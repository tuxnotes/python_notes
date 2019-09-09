from itertools import islice

f = open('/var/log/dpkg.log.1')

for line in islice(f, 100-1, 300): # 实际上是读了400行，前100行丢弃
    print(line)

def my_islice(iterable, start, end, step=1):
    tmp = 0 # 控制步长
    for i , x in enumerate(iterable):
        if i >= end:
            break

        if i >= start:
            if tmp == 0:
                tmp = step
                yield x
            tmp -= 1 # 当步长不为1，循环过程中i增加,tmp减小，但不yield。只有当tmp减小到0，此时i增加到了步长数,yield

print(list(my_islice(range(100,150),10,20,3)))
print(list(islice(range(100,150),10,20,3)))
