import os

s = os.stat('a.txt') # 第一个参数可以是一个文件或是文件描述符
fd = os.open('b.py', os.O_RDONLY)
os.read(fd, 10)
bin(s.st_mode)
os.stat('/proc')

# 硬链接 软连接

import stat

stat.S_IFDIR & s.st_mode
stat.S_IFCHR & s.st_mode
stat.S_IFREG & s.st_mode
stat.S_ISREG(s.st_mode)
os.stat('1.txt', follow_symlinks=False) # 等效os.lstat('1.txt')
stat.S_IRUSER & s.st_mode
stat.S_IXOTH & s.st_mode

import time

time.localtime(s.st_atime)

os.path.isdir('a.txt') # os.path没有文件权限的的方法
os.path.getatime('a.txt')
os.path.getsize('a.txt')

