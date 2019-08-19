# Exercise

### 1. Image an accounting routine used in a book shop. It works on a list with sublists, which look like this

| Order Number | Book Title and Author              | Quantity | Price per Item |
| ------------ | ---------------------------------- | -------- | -------------- |
| 34587        | Learning Python, Mark Lutz         | 4        | 40.95          |
| 98762        | Programming Python, Mark Lutz      | 5        | 56.80          |
| 77226        | Head First Python, Paul Barry      | 3        | 32.95          |
| 88112        | Einfuhrung in Python3, Bernd Klein | 3        | 24.99          |

Write a python program , which return a list with 2-tuples. Each tuple consist of a the order number and the product of the price per items and the quantity. The product should be increased by 10 $ if the value of the order is smaller than 100,00 $

Write a python program using lambda and map.

### 2 The same bookshop, but this time we work on a different list. The sublists of our lists look like this:

**[order number, (article number, quantity, price per unit), ... (article number, quantity, price per unit)]**

Write a program which returns a list of two tuples with (order number, total amount of order).

### Solutions to the Exercise

- Ex 1

```python
orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
	       ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein", 	3, 24.99]]
min_order = 100
invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10), map(lambda x: (x[0], x[2] + x[3]), orders)))
print(invoice_totals)
```

