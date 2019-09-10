from random import randint

chinese = [randint(60,100) for _ in range(20)]
math = [randint(60,100) for _ in range(20)]
english = [randint(60,100) for _ in range(20)]

t = []

for s1, s2, s3 in zip(chinese, math, english):
    t.append(s1 + s2 + s3)

[sum(s) for s in zip(chinese,math,english)]
# map也可以并行迭代，当处理函数简单的时候可以使用map
map(lambda s1, s2, s3: s1+s2+s3, chinese,math,english)

list(map(lambda *args: args, chinese, math, english))

from itertools import chain


