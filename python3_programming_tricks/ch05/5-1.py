"""

python2中

s = 'abc'
type(s)  # output <type 'str'>
# 一个字符在计算机中使用二进制数表示
bin(ord('a')) # output: '0b1100001'
# 最开始字符值考虑了英文字符，所以一个字节就可以表示一个字符
# 但中文等一个字节就不够了。但实际上unicode字符串才是真正意义上
# 的字符串。里面是一个一个字符，但一个字符用几个字节表示并不一定

一个字符(广义上，不知道英文，还包括中文等其他语言)，每个字符在
Python中只有唯一的一种表示，即unicode.但是将这些字符写入文件，
就不是唯一表示了。

Python2.x: 写入文件前，对unicode编码，读入文件后对字节进行解码
python2中一个文本就是一个unicode字符串
Python3.x: open函数指定't'的文本模式，encoding指定编码格式
"""

"""
以下代码在python2环境中

s = u'我爱Python。'
type(s) # output: <type 'unicode'>
f = open('a.txt','w') #
# write方法传入的是字节串，bytes串，也就是Python2中的str,
# 而我们这里是unicode,所以需要编码encode
f.write(s.encode('utf8'))
f.flush()
在Python2中拿到unicode要先编码，在写入

# 读取

f = open('a.txt')
txt = f.read()
# 在Python交互解释器中，输入txt回车，输出：'\xe6\x88....\x82'
type(txt) # output : <type 'str'>,说明我们读取的是string,python3中是bytes

# 读取的是字节，所以需要还原成unicode,需要解码decode

txt.decode('utf8') # 编码个解码要统一，否则会出现乱码
print(txt.decode('utf8')) # output: 我爱Python。
"""

"""
以下代码在python3中
s = u'我爱Python。'
type(s) # output: <type 'str'> 真正含义的字符串string
# python3中读写文件比较简单
f = open('b.txt','w', encoding='gbk')
# python3中多了一种新的打开方式，叫文本模式打开't'，‘t'可以不写，Python3默认以文本方式打开
# 文本模式打开与之前的区别：之前在写入和读取的时需要手动执行编解码
# 上面中的encoding没有指定的话，会使用系统的设置
f.write(s)
f.flush()

# shell中，cat b.txt则出现乱码，因为编码使用gbk，而cat使用的是
# 系统的utf8进行解码，所以出现了乱码

# 如果用Python程序去读取，就会读出原来的文本
f = open('b.txt', encodeing='gbk')
f.read() # 在交互解释其则输出：我爱Python。
"""
