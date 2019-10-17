
# [题目1] 斐波那契数列 (Fibonacci sequence):
# F(0) = 1, F(1) = 1, F(n)=F(n-1) + F(n-2) (n>=2)
# 求数列第n项的值？

def fibonacci(n):
    if n<= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
# 这里有个问题，就是在计算过程中包含大量重复计算

# [题目2] 走楼梯问题
# 有100阶楼梯，一个人每次可以迈1-3阶，一共有多少走法？

def climb(n, steps):
    count = 0
    if n == 0:
        count = 1
    elif n > 0:
        for step in steps:
            count += climb(n-step, steps)
    return count

# 上面的计算过程也包含大量重复

# 为了解决上面的问题，使用缓存

cache = {}

def fibonacii_cache(n):
    res = cache.get(n)
    if res:
        return res

    if n <= 1:
        return 1
    res = cache[n] = fibonacii_cache(n-1) + fibonacii_cache(n-2)
    return res

# 装饰器思路

# 构造生产包裹函数的工厂

def memo(func):
    cache = {}
    def wrap(*args):
        res = cache.get(args)
        if not res:
            res = cache[args] = func(*args)
        return res

    return wrap

fibonacii = memo(fibonacii)
print(fibonacii(50))

climb = memo(climb) # 等价于 @memo
print(climb(100, (1,2,3)))

