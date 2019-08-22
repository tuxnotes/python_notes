from random import randint
from collections import deque
import pickle
def guess(n, k):
    if n == k:
        print("猜对了，这个数字是%d" % k)
        return True

    if n < k:
        print('猜大了， 比%d小' % k)
    elif n > k:
        print('猜小了， 比%d大' % k)
    return False


def main():
    n = randint(1, 100)
    i = 1
    hq = deque([], 5) # 历史记录队列
    while True:
        line = input("[%d] 请输入一个数字" % i)
        if line.isdigit():
            k = int(line)
            hq.append(k)
            i += 1
            if guess(n ,k):
                break
        elif line == 'quit':
            break
        elif line == 'h?': # 查询接口
            print(list(hq))

if __name__ == '__main__':
    main()
