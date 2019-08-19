
from random import randint

# 生成分数表

d = {k: randint(60,100) for k in 'abcdefgh'}
l = [(v,k) for k,v in d.items()]
result = sorted(l)
print(result)

# zip方法,python3中zip返回生成器

l2 = list(zip(d.vaules(),d.keys()))
result2 = sorted(l2)
print(result2)


# 方案2

result3 = sorted(d.items(), key=lambda item: item[1], reverse=True)

# 使用enumerate

for i, (k,v) in enumerate(result3, 1):
    d[k] = (i,v)

# 使用字典解析

{k:(i,v) for i,(k,v) in enumerate(p,1)}
