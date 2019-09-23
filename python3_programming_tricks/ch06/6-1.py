
import csv

rf = open('books.csv')
csv.reader(rf) # 使用参数delimeter设置分割符

next(reader)

wf = open('demo.csv')
 writer = csv.writer(wf, delimiter=' ')
 writer.writerow(['x','y','z'])
 writer.writerow([1,2,3])
 writer.writerow([7,8,9])

 with open('books.csv') as rf:
     reader = csv.reader(rf)
     headers = next(reader)
     with open('books_out.csv', 'w') as wf:
         writer = csv.writer(wf)
         writer.writerow(headers)

         for book in book[-2]:
             if price and float(price) >= 80.00:
                 writer.writerow(book)

