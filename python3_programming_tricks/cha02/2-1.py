#!/usr/bin/env python3

data = [-1, 2, 3, -4 ,5]
res = []

for x in data:
    if x >= 0:
        res.append(x)

from random import randint

# 创建包含10个整数的随机列表

int_list = [randint(-10,10) for _ in range(10)] # 列表中并不需要循环变量
print(int_list)
# 使用列表解析过滤
[ x for x in int_list if x >= 0 ]

# 使用filter函数
# filter函数接受两个参数: 第一个参数传入一个过滤函数，第二个参数是需要过滤的对象，如列表
# 过滤函数一般使用lambda匿名函数： lambda x: x >= 0
# python3中filter函数返回的是生成器对象

g = filter(lambda x: x >= 0, int_list)
res = list(g)
print(res)

scores = {'student%d' % i: randint(50, 100) for in range(1,21)}
score_res = {k:v for k,v in scores.items() if v >= 90}
print(score_res)
score_g = filter(lambda item: item[1] >= 90, scores.items())
# scores.items() gives a tuple per iteration, and the index 0 is the key, index 1 is the value
result = dict(score_g)
rand_set = {randint(0,20) for _ in range(20)}
set_result = { x for x in rand_set if x % 3 == 0}

