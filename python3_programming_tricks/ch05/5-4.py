# 先创建一个大小为1MB，内容全是0的文件
# dd if=/dev/zore of=demo.bin bs=1024 count=1024
# od -x demo.bin

import mmap

f = open('demo.bin', 'r+b')
f.fileno() # 获取文件描述符，也可以通过os.open()打开文件获得文件描述符

# 映射以页为单位，通过mmap.PAGESIZE查看页大小
m = mmap.mmap(f.fileno(), 0)
m.write(b'abc')
m[0]
m[5]
m[5] = 78
m[8:16] = b'\xff' * 8

# ls /dev/fb0 (framebuffer)
# fbset

f = open('/dev/fb0', 'r+b')
size = 1920 * 1080 * 4
m = mmap.mmap(f.fileno(), size)
m[:size/2] = b'\xff\xff\xff\x00' * (size // 4 // 2) # 屏幕的一半为白色
m.close()
f.close()

