import xml.etree.ElementTree as ET

data = ET.Element('Data')
book = ET.Element('Book')
author = ET.Element('作者')
book.set('x', 'abc')
author.text('刘硕')
data.append(book)
data.append(author)
ET.dump(data)
book = ET.SubElement(data, 'Book')
book.set('x', 'abc')
author = ET.subElement(book, '作者')
author.text = '刘硕'
et = ET.ElementTree(data)
et.write('test.xml', encoding='utf8')

import csv
from xml.etree.ElementTree import ElementTree, Element, SubElement

def csv_to_xml(csv_path, xml_path):
    with open(csv_path) as f:
        reader = csv.reader(f)
        headers = next(reader)

        root = Element('Data')
        root.text = '\n\t'
        root.tail = '\n'

        for row in reader:
            book = SubElement(root, 'Book')
            book.text = '\n\t\t'
            book.tail = '\n\t'
            for tag, text in zip(headers, row):
                e = SubElement(book, tag)
                e.text = text
                e.tail = '\n\t\t'
            e.tail = '\n\t'


        ElementTree(root).write(xml_path, encoding='utf8')


csv_to_xml('books.csv', 'books.xml')

# 在vim中命令模式下， :tabnew books.xml就可以打开books.xml

