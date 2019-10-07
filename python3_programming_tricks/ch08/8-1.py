# 此版本是使用串行的方式顺序下载
import requests
import base64
from io import StringIO
import csv
from xml.etree.ElementTree import ElementTree, Element, SubElement

USERNAME = b'7f304a2df40829cd4f1b17d10cda0304'
PASSWORD = b'aff978c42479491f9541ace709081b99'

def download_csv(page_number):
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

def csv_to_xml(csv_file, xml_path):
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

def download_and_save(page_number, xml_path):
    # IO
    csv_file = None
    while not csv_file:
        csv_file = download_csv(page_number)
    # CPU
    csv_to_xml(csv_file, 'data%s.xml' % page_number)

if __name__ == "__main__":
    import time
    t0 = time.time()
    for i in range(1, 6):
        download_and_save(i, 'data%s.xml' % i)
    print(time.time() - t0)
    print('main thread end.')

