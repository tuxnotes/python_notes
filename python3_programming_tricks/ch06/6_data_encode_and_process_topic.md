
# 6 数据编码与处理话题

## 6.1 如何读写csv文件

**实际案例**

我们编写网络爬虫从豆瓣爬去了一些书籍的信息，以csv数据格式存储：

书名,作者,出版社,价格
江铜scrapy网络爬虫,刘硕,清华大学出版社,46.00
算法导论,Charles E.Leiserson,人民邮电出版社,85.00
Python灰帽子,Justin Seitz,电子工业出版社,39.00
.......

请将书价格高于80.00的数记录存储到另一个csv文件中。

**解决方案**

使用标准库中的csv模块，使用其中的reader和writer完成csv文件读写

## 6.2 如何读写json数据

**实际案例**

在web应用中常用JSON(JavaScript Object Notation)格式传输数据，如：

1. 利用http://httpbin.org/API对发送的http请求进行观测
2. 爬虫程序利用Splash渲染引擎渲染页面

在Python中如何读写json数据？

**解决方案**

标准库中的json模块，使用其中loads,dumps函数完成json数据的读写

## 6.3 如何解析简单的xml文档

**实际案例**

xml是极为常用的标记性语言，可提供统一的方法来描述应用程序的结构话数据：

<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
</data>

python中如何解析xml文档

**解决方案**

使用标准库中的xml.etree.ElementTree
xml是数树状结构
