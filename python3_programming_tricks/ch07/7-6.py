# 描述即是一个接口，在进行__dict__添加属性的时候进行检查
# 描述符就是包含如下__set__ __get__ __del__方法的类

class Descriptor:
    def __init__(self, key):
        self.key = key
        self.type_ = type_
    def __set__(self, instance, value):
        print('in __set__')
        if not isinstance(value, self.type_):
            raise TypeError('must be %s' % self.type_)
        instance.__dict__[self.key] = value

    def __get__(self, instance, cls):
        print(''in __get__), instance, cls
        return instance.__dict__[self.key]

    def __delete__(self, instance):
        print('in __del__', instance)
        del instance.__dict__[self.key]


class Person:
    name = Attr('name', str)
    age = Attr('age', int)

p = Person()

p.name = 'liushuo'
p.age = '32'
# a = A()
# a.x = 5 # 调用__set__
# print(a.x) # 调用__get__

