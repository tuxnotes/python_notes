from random import randint, sample
sample('abcdefgh',randint(3,6))

# 第1轮

d1 = {k: randint(1,4) for k in sample('abcdefgh',randint(3,6))}
# 第2轮
d2 = {k: randint(1,4) for k in sample('abcdefgh',randint(3,6))}
# 第3轮
d3 = {k: randint(1,4) for k in sample('abcdefgh',randint(3,6))}

# solution 1
# find 公共键

[k for k in d1 if k in d2 and k in d3]

dl = [d1,d2,d3]

[k for k in dl[0] if all(map(lambda d: k in d, dl[1:]))]

# solution 2

# python3 中reduce不是内置函数，在functools标准库中。Python2是内置函数，

from functools import reduce

reduce(lambda a, b: a & b ,map(dict.keys,dl))
