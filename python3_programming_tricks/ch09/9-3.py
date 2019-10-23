# 迭代两个字典:先以参数的名称作为key,以参数的类型作为value创建一个字典
#

import inspect

def type_assert(*ty_args, **ty_kwargs):
    def decorator(func):
        # A...
        func_sig = inspect.signature(func)
        bind_type = func_sig.bind_partial(*ty_args, **ty_kwargs).arguments
        def wrap(*args, **kwargs):
            # B...
            for name, obj in func_sig.bind_partial(*args, **kwargs).arguments.items():
                type_ = bind_type.get(name)
                if type_:
                    if not isinstance(obj, type_):
                        raise TypeError('%s must be %s', % (name, type_))
            return func(*args, **kwargs)
        return wrap
    return decorator

@type_assert(int, list, str)
def f(a, b, c):
    pass

f(5, [], 'abc') # 正确的参数类型
f(5, 10, 'abc') # 错误的参数类型

@type_assert(c= str) # 只检查c是否是str
def f(a, b, c):
    pass
