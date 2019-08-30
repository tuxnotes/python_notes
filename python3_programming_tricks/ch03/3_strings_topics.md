
# 3 String Related

## 3.1 如何查分有多种分隔符的字符串

**实际案例**

把某个字符串依据分隔符号拆分不同的字段。该字符串包含多种不同的分隔符，例如：

s = 'ab;cd|dfg|hi,jkl|mn\topq;rst,uvw\txyz'

其中<,>,<;>,<|>,<\t>都是分隔符，如何处理？

**解决方案**

方法1：连续使用str.split()方法，每次处理一种分隔符号。一次只能处理一种分隔符；
方法2：使用正则表达式的re.split()方法。(推荐)

## 3.2 如何判断字符串a是否以字符串b开头会结尾

**实际案例**

某文件系统目录下有一系列文件：

quicksort.c
graph.py
heap.java
install.sh
stack.cpp
...

编写程序给其中所有的.sh文件和.py文件加上用户可执行权限

**解决方案**

使用str.startswith()和str.endswith()方法。(注意：多个匹配时参数使用元组.)

## 3.3 如何调整字符串中文本的格式

**实际案例**

某软件的log文件，起哄的日期格式为 'yyyy-mm-dd':

2016-05-21 10:39:26 status unpacked python3-pip:all
2016-05-23 10:49:26 status half-configured python3
2016-05-23 10:52:26 status installed python3-pip:all
2016-05-24 11:57:26 configure python3-wheel:all 0.24
...

如果把其中日期改为美国日期的格式 'mm/dd/yyyy',如


'2016-05-23' => '05/23/2016', 应如何处理

**解决方案**

使用正则表达式re.sub()方法做字符串替换，利用正则表达是的捕获组，捕获每个部分内容，在替换字符串中调整各捕获组的顺序。

## 3.4 如何将多个小字符串拼接成一个大字符串

**实际案例**

在设计某网络程序时，我们自定义了一个基于UDP的网络协议，按固定次序向服务器传递一系列参数：

hwDetect:       "<0112>"