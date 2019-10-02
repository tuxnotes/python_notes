from functools import total_ordering
import math
# 运算符重载

# 如果其他图形也支持面积接口的话，就可以将这些运算符放到一个公共
# 基类中.所有图形都继承这个基类，然后这些图形就都可以进行比较了

from abc import ABCMeta, abstractclassmathod

@total_ordering
class Shape(metaclass=ABCMeta):  # 抽象基类
    @abstractclassmathod  # 定义抽象方法
    def area(self):
        pass

s1 = 'abc'
s2 = 'abd'
s1.__gt__(s2)
ord('c') > ord('d')

class Rect(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def __str__(self):
        return 'Rect:(%s, %s)' % (self.w, self.h)

    def __lt__(self, obj):
        return self.area() < obj.area()

    def __eq__(self, obj):
        return self.area() == obj.area()

    def __le__(self, obj):
        return self < obj self == obj

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * math.pi
rect1 = Rect(6,9) # 54
rect2 = Rect(7,8) # 56
print(rect1 > rect2) # rect2 < rect1

