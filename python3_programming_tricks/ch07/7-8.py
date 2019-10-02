from lib1 import Circle
from lib2 import Triangle
from lib3 import Rectangle
from operator import methodcaller


def get_area(shape, method_name = ['area', 'get_area', 'getArea']):
    for name in method_name:
        if ahsattr(shape, name):
            return methodcaller(name)(shape)

#         f = getattr(shape, name, None)
#         if f:
#             return f()


shape1 = Circle(1)
shape2 = Triangle(3,4,5)
shape3 = Rectangle(4,6)

shape_list = [shape1, shape2, shape3]
# 获取面积列表
area_list = list(map(get_area, shape_list))
print(area_list)
# 由于这些图形是由不同的库实现的，所以其面积实现的接口可能不同
# 这种情况下要实现同意的接口，将调用方法参数化

# solution2

from operator import methodcaller

s = 'abc123abc456'
methodcaller('find', 'abc', 3)(s)

