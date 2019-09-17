f = open('a.bin', 'wb')
f.write(b'abc') # 此时并没有写入磁盘，还在缓冲区
f.write(b'efg')
# 磁盘的缓冲去大小是磁盘的属性，dmesg | grep block查看
# Python缓冲区大小默认是4096.如果Python找不到磁盘块打下则使用如下方式：

import io

io.DEFAULT_BUFFER_SIZE # 找不到则使用此值

f.write(b'+' * (4096-6)) # 凑4096字节
f.write(b'-') # -号并没有输出，在缓冲区的第0个位置

# 文本模式下的缓冲区行为

f2 = open('a.txt','w') # 文本模式下写入的是字符串，但缓冲区是按字节计算.注意汉字编码后是三个字节，因此选用ASCII便于计算
f2.write('a' * 4095)
f2.write('bc')
f2.write('+' * 999) # 到这里已经写入5096，但是另一个终端tail -f还是没有输出
# 原因是三层模型

# 二进制打开时，f是一个_io.BufferWriter
# 文本方式打开时，f2是一个_io.TextIOWrapper
# f2.buffer是_io.BufferWriter
# f.raw 是 _io.FileIO

f2.write('*'*(8192-5096))

# 行缓冲，遇到换行才写入磁盘，通常交互式设备是行缓冲，如终端，也是一个文件，属于charactor device字符设备
# tty命令可以查看当前交互的终端是哪个文件

f3.open('/dev/pts/2','w')
f3.istty # 返回True

f3.write('abc')
f3.write('efg')
f3.write('\n') # 行缓冲要以文本模式读写

# 手动指定缓冲行为

f4 = open('a.bin','wb', buffering=8192) # 二进制默认是4096
f4.write(b'+' * 4097)
f4.write(b'-' * 4097)

# 二进制下无缓冲

f4.raw.write(b'abc') # tail -f 中直接输出
# 或用下面方式实现无缓冲
f4 = open('a.bin','wb', buffering=0) # 二进制默认是4096

# 设置行缓冲，行缓冲只能对文本模式

f2 = open('a.txt', 'w', buffering=1)
f2.write('abc')
f2.write('efg')
f2.write('\n')


