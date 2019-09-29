# 这里用两种方式定了palyer类，一种是palyer1,一种是palyer2


class Player1:
    def __init__(self, uid, name, level):
        self.uid = uid
        self.name = name
        self.level = level


class Player2:
    __slots__ = ['uid', 'name', 'level'] # 类属性
    def __init__():
        self.uid = uid
        self.name = name
        self.level = level


p1 = Player1('0001', 'Jim', 20)
p2 = Player2('0001', 'Jim', 20)
dir(p1)
dir(p2)
set(dir(p1)) - set(dir(p2))  # 主要浪费内存的地方是__dict__，其用于动态属性的维护
p1.__dict__['z'] = 300 # 等同于p1.z = 300

import sys

sys.getsizeof(p1.__dict__) # 864 bytes
sys.getsizeof(p1.name) # 52 bytes
sys.getsizeof(p1.level) # 28 bytes
sys.getsizeof(p1.uid) # 53 bytes

# 为了避免内存的浪费，就关闭动态属性
# p2.x = 1 # AttributeError

# 测试

import tracemalloc  # 跟踪内存使用

tracemalloc.start()
# start
la = [Player1(1,2,3) for _ in range(100000)]
#lb = [Player2(1,2,3) for _ in range(100000)]
# end
snapshot = tracemalloc.take_snapshot()
#top_stats = snapshot.statistics('lineno')
top_stats = snapshot.statistics('filename')
for stat in top_stats[:10]: print(stat)


