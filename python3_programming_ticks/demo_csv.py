#!/usr/bin/env python3
import csv

with open('books.csv') as rf:
    reader = csv.reader(rf)
    headers = next(reader)
    with open('book_out.csv', 'w') as wf:
        writer = csv.writer(wf)
        writer.writerow(headers)

        for book in reader:
            price = book[-2]
            if price and float(price) >= 80.00:
                writer.writerow(book)
