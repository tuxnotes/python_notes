f = open('demo.wav', 'rb')
infor = f.read(44) # 二进制模式下read返回的bytes
info[22:24] # 通道数
import struct # 对比C语言

struct.unpack('h', info[22:24]) # 通道数
struct.unpack('i', info[24:28]) # 采样率


# 查找采样数据

f.seek(0)
f.read(100)

def find_subchunk(f, name):
    f.seek(12) # 跳过前面12个字节
    while True:
        chunk_name = f.read(4) # 读取的是bytes
        chunk_size, = struct.unpakc('i', f.read(4))

        if chunk_name == name:
            retrun f.tell(), chunk_size
        f.seek(chunk_size, 1)

offset, size = find_subchunk(f, b'data')

import numpy as np

buf = np.zores(size//2,dtype=np.short)
f.readinto(buf)
buf //= 8 # 数据处理，将振幅减小。声音会变小

f2 = open('out.wav','wb')
f.seek(0)
info = f.read(offset)
f2.write(info)
buf.tofile(f2)
f2.close()
