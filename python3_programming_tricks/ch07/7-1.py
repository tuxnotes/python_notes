

class IntTuple(tuple):
    def __new__(cls, iterable):
        # 过滤iterable，然后将结果返回给父类
        # tuple 没有实现__init__ , tuple.__init__ is object.__init__ 返回True
        f_it = (for e in ietrable if isinstance(e, int) and e > 0)
        return super().__new__(cls, f_it)





int_t = IntTuple([1, -1, 'abc', 6, ['x','y'],3])
print(int_t)
