# 5 File IO related

## 5.1 如何读写文本文件

**实际案例**

文件读写本来是一个很简单的问题，但是python2与python3版本的不同，读写有一定的差别。

某文本文件编码格式已知(如UTF-8,GBK,BIG5)，在python2.x和python3.x中分别如何读写该文件。

文本文件就是由一些字符构成

**解决方案**

字符串的语义发生了变化：

Python2     Python3

str     ->  bytes
unicode ->  str

Python2.x: 写入文件前，对unicode编码，读入文件后对字节进行解码
python2中一个文本就是一个unicode字符串
python2中操作的是字节串，bytes,写入前要编码，读取后要解码

Python3.x: open函数指定't'的文本模式，encoding指定编码格式

# addendum

## Definitions

A **character** is the smallest possible component of a text. ‘A’, ‘B’, ‘C’, etc., are all different characters. So are ‘È’ and ‘Í’. Characters are abstractions, and vary depending on the language or context you’re talking about.

The Unicode standard describes how characters are represented by **code points**. A **code point** is an integer value, usually denoted in base 16. In the standard, a code point is written using the notation U+12ca to mean the character with value 0x12ca (4810 decimal). The Unicode standard contains a lot of tables listing characters and their corresponding code points:

```
0061    'a'; LATIN SMALL LETTER A
0062    'b'; LATIN SMALL LETTER B
0063    'c'; LATIN SMALL LETTER C
...
007B    '{'; LEFT CURLY BRACKET
...
2167    'Ⅷ'; ROMAN NUMERAL EIGHT
2168    'Ⅸ'; ROMAN NUMERAL NINE
...
265E    '♞'; BLACK CHESS KNIGHT
265F    '♟'; BLACK CHESS PAWN
...
1F600   '😀'; GRINNING FACE
1F609   '😉'; WINKING FACE
...
```

字符是文本的最小组成单元，是一种抽象，与语言很相关。Unicode标准描述了字符如何通过code point来表示。code point是十六进制数。

## Encoding

**Python2 docs**

To summarize the previous section: a Unicode string is a sequence of code points, which are numbers from 0 to 0x10ffff. This sequence needs to be represented as a set of bytes (meaning, values from 0–255) in memory. The rules for translating a Unicode string into a sequence of bytes are called an encoding.

The first encoding you might think of is an array of 32-bit integers. In this representation, the string “Python” would look like this:

```
   P           y           t           h           o           n
0x50 00 00 00 79 00 00 00 74 00 00 00 68 00 00 00 6f 00 00 00 6e 00 00 00
   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
```

This representation is straightforward but using it presents a number of problems.

It’s not portable; different processors order the bytes differently.

It’s very wasteful of space. In most texts, the majority of the code points are less than 127, or less than 255, so a lot of space is occupied by zero bytes. The above string takes 24 bytes compared to the 6 bytes needed for an ASCII representation. Increased RAM usage doesn’t matter too much (desktop computers have megabytes of RAM, and strings aren’t usually that large), but expanding our usage of disk and network bandwidth by a factor of 4 is intolerable.

It’s not compatible with existing C functions such as strlen(), so a new family of wide string functions would need to be used.

Many Internet standards are defined in terms of textual data, and can’t handle content with embedded zero bytes.

Generally people don’t use this encoding, instead choosing other encodings that are more efficient and convenient. UTF-8 is probably the most commonly supported encoding; it will be discussed below.

Encodings don’t have to handle every possible Unicode character, and most encodings don’t. For example, **Python’s default encoding is the ‘ascii’ encoding**. The rules for converting a Unicode string into the ASCII encoding are simple; for each code point:

If the code point is < 128, each byte is the same as the value of the code point.

**If the code point is 128 or greater, the Unicode string can’t be represented in this encoding. (Python raises a UnicodeEncodeError exception in this case.)**

reference: https://docs.python.org/2.7/howto/unicode.html

**Python3 docs**

To summarize the previous section: a Unicode string is a sequence of code points, which are numbers from 0 through 0x10FFFF (1,114,111 decimal). This sequence of **code points** needs to be represented in memory as a set of **code units**, and **code units** are then mapped to 8-bit bytes. The rules for translating a Unicode string into a sequence of bytes are called a **character encoding**, or just an **encoding**.

The first encoding you might think of is using 32-bit integers as the code unit, and then using the CPU’s representation of 32-bit integers. In this representation, the string “Python” might look like this:

```
   P           y           t           h           o           n
0x50 00 00 00 79 00 00 00 74 00 00 00 68 00 00 00 6f 00 00 00 6e 00 00 00
   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
```

This representation is straightforward but using it presents a number of problems.

It’s not portable; different processors order the bytes differently.

It’s very wasteful of space. In most texts, the majority of the code points are less than 127, or less than 255, so a lot of space is occupied by 0x00 bytes. The above string takes 24 bytes compared to the 6 bytes needed for an ASCII representation. Increased RAM usage doesn’t matter too much (desktop computers have gigabytes of RAM, and strings aren’t usually that large), but expanding our usage of disk and network bandwidth by a factor of 4 is intolerable.

It’s not compatible with existing C functions such as strlen(), so a new family of wide string functions would need to be used.

Therefore this encoding isn’t used very much, and people instead choose other encodings that are more efficient and convenient, such as UTF-8.

**UTF-8 is one of the most commonly used encodings, and Python often defaults to using it**. UTF stands for “Unicode Transformation Format”, and the ‘8’ means that 8-bit values are used in the encoding. (There are also UTF-16 and UTF-32 encodings, but they are less frequently used than UTF-8.) UTF-8 uses the following rules:

If the code point is < 128, it’s represented by the corresponding byte value.

If the code point is >= 128, it’s turned into a sequence of two, three, or four bytes, where each byte of the sequence is between 128 and 255.

reference: https://docs.python.org/3/howto/unicode.html

# Conclusion

encoding:是一种规则，将unicode string转换成内存bytes(8-bit)单个字节表示的规则
Python2: 默认encoding是 ascii
Python3：默认encoding是 utf8

## 5.2 如何处理二进制文件

**实际案例**

wav是一种音频文件的格式，音频文件为二进制文件。
wav文件由头部信息和音频采用数据构成。前面为头部信息，包括声道数，
采样频率，编码位宽等等，后面是音频采样数据。

使用Python，分析一个wav文件头部信息，处理音频数据。

**解决方案**

open函数想以二进制模式打开文件，指定mode参数为'b'
二进制数据可以用readinto，读入到提前分配好的buffer中
解析二进制数据可以使用标准库中的struct模块中的unpack方法

## 5.3 如何设置文件的缓冲

**实际案例**

在Python程序里，一个文件的内容是在内存中。如果将内存中的内容写入
到硬件设备(磁盘)时，需要使用系统调用(系统提供的服务).这类的I/O操
作通常是很费时的。并且由于磁盘属于块设备，读写的时候并不是按一个
字节一个字节的进行读写，是按块(如4096字节)进行读写。因此写一个
字节和写4096个字节耗时是一样的。为了减少I/O操作的次数，文件通常
使用缓冲区(不是来一个字节写一些字节，而是先收集这些字节，有足够
多的数据,凑够一个块大小的数据时才进行系统调用).文件缓冲行为，分为
全缓冲，行缓冲，无缓冲。

如何设置Python文件对象的缓冲行为

全缓冲：缓冲区大小固定，直到缓冲区被充满，才写入磁盘

Python默认是全缓冲行为

三层模型

Raw(无缓冲) --> B(有缓冲4096)二进制 --> TextIO文本模式(有缓冲8192)

**解决方案**

全缓冲：open函数的buffering设置为大于1的整数n,(n为缓冲区大小)

行缓冲：open函数的buffering设置为1(只能针对文本模式)

无缓冲：open函数的buffering设置为0

## 5.4 如何将文件映射到内存

**实际案例**

1. 在访问某些二进制文件是，希望把文件映射到内存中，可以实现随机访问(framebuffer设备文件)

2. 某些嵌入式设备，集群器被编址到内存地址空间，我们可以映射/dev/mem某范围，去访问这些寄存器。

3. 如果多个进程映射同一个文件，还能实现进程间通信的目的

**解决方案**

使用标准库中mmap.mmap()函数，将文件映射到进程的内存地址空间

## 5.5 如何访问文件的状态

**实际案例**

在某些项目中，需要获取文件的状态，通常文件的状态包含一下几种：
1. 文件的类型(普通文件,目录,符号链接,设备文件...)
2. 文件的访问权限
3. 文件的最后的访问/修改/节点状态更改时间
4. 普通文件的大小

**解决方案**

系统调用：标准库os模块中的系统调用stat获取文件状态
快捷函数：os.path下一些函数，使用起来更加简洁

## 5.6 如何使用临时文件

**实际案例**

某项目中，我们重传感器采集数据，没收集到1G数据后，做数据分析，最终只保存分析结果。
这样大量的临时数据如果常驻内存的话，将消耗大量内存资源，我们可以使用临时文件存储这些临时数据(外部存储).
临时文件不用命名，且关闭后会自动被删除

**解决方案**

使用标准库中的TemporaryFile以及NamedTemporaryFile
通常情况下使用TemporaryFile即可，在多进程的情况下可以使用NamedTemporaryFile
