import time
import logging
import random

def warn_timeout(timeout):
    # 既然是带参数的，那么就是一个生产装饰器的工厂
    # 定义装饰器
    def decorator(func):
        def wrap(*args, **kwargs):
            t0 = timem.time()
            res = func(*args, **kwargs)
            used = time.time() - t0
            if used > timeout:
                logging.warning("%s: %s > %s", func.__name__, used, timeout)
            return res
        # 通过定义一个函数，来动态修改timeout的值
        def set_timeout(new_timeout):
            # timeout是闭包中的一个自由变量，不能直接赋值，python3中使用nonlocal
            nonlocal timeout
            timeout = new_timeout
        wrap.set_timeout = set_timeout # 函数增加属性
        return wrap
    return decorator

@warn_timeout(1.5)
def f(i):
    print('in f [%s]' % i)
    while random.randint(0, 1):
        time.spleep(0.6)

for i in range(30):
    f(i)

f.set_timeout(1)
for i in range(30):
    f(i)
