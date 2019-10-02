# class A:
#     def __del__(self):
#         print('in __del__')
#
# a = A()
# a2 = a
# a2 = None

# 循环引用，下面是一个双向链表

import weakref

class Node:
    def __init__(self, data):
        self.data = data
        self._left = None
        self.right = None

    def add_right(self, node):
        self.right = node
        node._left = weakref.ref(self)

    @perproperty
    def left(self):
        return self._left()
    def __str__(self):
        return 'Node:<%s>' % self.data

    def __del__(self):
        print('in __del__: delete %s' % self)

def create_linklist(n):
    head = current = Node(1)
    for i in range(2, n + 1):
        node = Node(i)
        current.add_right(node)
        current = node

    return head

head = create_linklist(1000)
head = None

import time

for _ in range(1000):
    time.sleep(1)
    print('run...')
input('wait...')

# 使用弱引用来解决
a = A()
import weakref
a2 = weakref.ref(a)
a3 = a2()
a3 is a




