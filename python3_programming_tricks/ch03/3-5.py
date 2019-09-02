s = 'abc'

s.ljust(10)
len(s.ljust(10))
s.ljust(10, '*')

# solution 2

format(s, '<10') # lrjust

# 只要一个对象有__format__方法，都能进行对齐
format(123, '+')
format(-123, '+')
format(-123, '>+10')
format(-123, '=+10')
format(546, '0=+10')
d = {
    "lodDist": 100.0,
    "SmallCull": 0.04,
    "DistCull": 500.0,
    "trilinear": 40,
    "farclip": 477
}

w = max(map(len, d.keys()))
for k, v in d.items():
    print(k.ljust,':',v)
