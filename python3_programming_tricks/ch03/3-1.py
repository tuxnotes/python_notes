
s = 'ab;cd|dfg|hi,jkl|mn\topq;rst,uvw\txyz'
s.split(';')
[ss.split('|') for ss in s.split(';')]
map(lambda ss: ss.split('|'), s.split(';'))
list(map(lambda ss: ss.split('|'), s.split(';')))
# 二维列表变成一维列表

t = []

list(map(t.extend, [ss.split('|') for ss in s.split(';')]))

# 或用下面的方式

sum([ss.split('|') for ss in s.split(';')], []) # sum默认初值为0

def my_split(s, seps):
    res = [s]
    for sep in seps:
        t = []
        list(map(lambda ss: ss.split(sep),res))
        res = t
    return res

# 采用reduce方式,此种方法用来熟练函数式编程，工程中尽量避免，因为代码的可读性差

from functools import reduce

reduce(lambda l, sep: sum(map(lambda ss: ss.split(sep), l),[]),',;|\t', [])
my_split2 = lambda s, seps: reduce(lambda l, sep: sum(map(lambda ss: ss.split(sep), l),[]),seps, [s])
my_split2(s, ';,|\t')

# solution 2
import re
re.split('[;,|\t]+', s)
