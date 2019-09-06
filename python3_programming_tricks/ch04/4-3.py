from decimal import Decimal
class FloatRange:
    def __init__(self, a, b, step):
        self.a = Decimal(str(a))
        self.b = Decimal(str(b))
        self.step = Decimal(str(step))

    def __iter__(self):
        t = self.a
        while t <= self.b:
            yield float(t)
            t += self.step

    def __reserved__(self):
        t = self.b
        while t >= self.a:
            yield float(t)
            t -= self.step

fr = FloatRange(3.0, 4.0, 0.2)
for x in fr:
    print(x)
print('-' * 20)
for x in reversed(fr):
    print(x)

# 由于是用十进制表示的浮点数，而在计算机中是用二进制，这样出现的
# 误差就会积累，使用标准库decimal处理

# from decimal import Decimal
# from functools import reduce
#
# reduce(Decimal.__add__, [Decimal(0.2)] * 20)
