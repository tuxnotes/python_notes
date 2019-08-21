
from random import randint

data = [randint(0,20) for _ in range(30)]

d = dict.fromkeys(data,0)

for x in data:
    d[x] += 1

#sorted([(v,k) for k,v in d.items()], reverse=True)
sorted(((v,k) for k,v in d.items()), reverse=True)

# 前3个
sorted(((v,k) for k,v in d.items()), reverse=True)[:3]

import heapq

heapq.nlarest(3,((v,k) for k,v in d.items()))


# solution2

from collections import Counter

c = Counter(data)
c.most_common(3)

# 英文文章词频统计

import re

txt = open('example.txt').read()

# 使用正则将文本切割，使用非字母字符进行切割

word_list = re.split('\W+',txt)
c2 = Counter(word_list)
# 频度最高的前10个
c2.most_common(10)

