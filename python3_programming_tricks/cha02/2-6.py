
from collections import OrderedDict
from random import shuffle # shuffle , disorder

players = list('abcdefgh')
shuffle(players)
od=OrderedDict() # od不支持切片操作

for i, p in enumerate(players, 1):
    od[p] = 1

def query_by_name(d, name):
    return d[name]


from itertools import islice

def query_by_order(d,a,b=None):
    a -= 1
    if b is None:
        b = a + 1
    return list(islice(od, a, b))
