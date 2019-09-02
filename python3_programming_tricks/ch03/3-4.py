s1 = 'abcdef'
s2 = '12345' # +号调用的是str.__add__方法
s1 + s2
l = ["<0112>","<32>","<1024x768>","<60>","<1>","<100.0>","<500.0>"]
s = ''
for x in l:
    s += x

from functools import reduce
reduce(str.__add__, l)

# 上面的过程中创建了大量的中间过程字符串，浪费了空间和时间

# solution2 recommanded
result = ''.join(l)
