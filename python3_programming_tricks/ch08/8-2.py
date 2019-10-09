# 此版本是使用线程方式并发下载
import requests
import base64
from io import StringIO
import csv
from queue import Queue
from threading import Thread
from xml.etree.ElementTree import ElementTree, Element, SubElement

USERNAME = b'7f304a2df40829cd4f1b17d10cda0304'
PASSWORD = b'aff978c42479491f9541ace709081b99'

# class MyThread(Thread):
#     def __init__(self, page_number, xml_path):
#         super().__init__() # 需要调用父类的构造器
#         self.page_number = page_number
#         self.xml_path = xml_path
#     def run(self):
#         download_and_save(self.page_number, self.xml_path)

class DownloadThread(Thread):
    def __init__(self, page_number, queue):
        super().__init__() # 需要调用父类的构造器
        self.page_number = page_number
        self.queue = queue

    def run(self):
        csv_file = None
        while not csv_file:
            csv_file = self.download_csv(self.page_number)
        self.queue.put(self.page_number, csv_file)

    def download_csv(self, page_number):
        print('download csv data [page=%s]' % page_number)
        url = 'http://api.intrinio.com/prices.csv?ticker=AAPL&hide_paging=true&page_size=200&page_number=%s' % page_number
        auth = b'Basic ' + base64.b64encode(b'%s:%s' % (USERNAME, PASSWORD))
        headers = {'Authorization': auth}
        response = requests.get(url, headers=headers)

        # 这里不将下载的数据保存到磁盘，因为后面还需要转换
        # 如果保存到磁盘，后面转换还需要读入内存。所以将下
        # 载的csv文件保存到内存中的文件StringIO
        if response.ok:
            return StringIO(response.text)

class ConvertThread(Thread):
    def __init__(self, queue):
        super().__init__() # 需要调用父类的构造器
        self.queue = queue

    def run(self):
        while True:
            page_number, csv_file = self.queue.get()
            self.csv_to_xml(csv_file, 'data%s.xml' % page_number)

    def csv_to_xml(self, csv_file, xml_path):
        print('Convert csv data to %s' % xml_path)
        reader = csv.reader(csv_file)
        headers = next(reader)

        root = Element('Data')
        root.text = '\n\t'
        root.tail = '\n'

        for row in reader:
            book = SubElement(root, 'Row')
            book.text = '\n\t\t'
            book.tail = '\n\t'

            for tag, text in zip(headers, row):
                e = SubElement(book, tag)
                e.text = text
                e.tail = '\n\t\t'
            e.tail = '\n\t'

        ElementTree(root).write(xml_path, encoding='utf8')

# def download_and_save(page_number, xml_path):
#     # IO python的多线程一般对IO密集型任务能加速
#     csv_file = None
#     while not csv_file:
#         csv_file = download_csv(page_number)
#     # CPU
#     csv_to_xml(csv_file, 'data%s.xml' % page_number)



if __name__ == "__main__":
    queue = Queue()
    thead_list = []
    for i in range(1, 6):
        t = DownloadThread(i, queue)
        t.start()
        thread_list.append(t)

    convert_thread = ConvertThread(queue)
    convert_thread.start()

    for t in thread_list:
        t.join() # waiting for child thread
    print('main thread end.')

