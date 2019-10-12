# 8 多线程与多进程相关话题

## 8.1 如何使用多线程

**实际案例**

https://intrinio.com/tutorial/web_api
通过上述网站提供的API获取过时信息的csv数据，现在要下载大量csv数据文件，并将其转换为xml文件。

如何使用线程来提高下载并处理的效率

网站注册后会生成用户名和密码，网站就是通过这个账号和密码对请求进行验证的。

**解决方案**

使用标准库threading.Thread创建线程，在每一个线程中下载并转换一只股票数据。


## 8.2 如何线程间通信

**实际案例**

前面从intrinio.com下载多只股票的csv数据， 并将其转换为xml文件

在Python中由于全局解释锁(GIL)的存在，多线程进行CPU密集型操作并不能提高执行效率，我们修改程序架构：
1. 使用多个DownloadThread线程进行下载(I/O)
2. 使用一个ConvertThread线程进行转换(CPU)
3. 下载线程把下载数据安全地传递给转换线程

GIL属于进程，不同进程中的GIL是相互独立的

**解决方案**

使用标准库中的queue.Queue,它是一个线程安全的队列

1. Download 线程把下载数据放入队列
2. Convert线程从队列里提取数据

## 8.3 如何在线程间进行事件通知

**实际案例**

上节课中，我们从intrinio.com下载多只股票的csv数据，并将其转换为xml文件。

额外需求：

实现一个线程TarThread,将转换出的xml文件压缩打包，比如转换线程没生产出100个xml文件，就通知打包线程将他们打包成一个xxx.tgz文件，并删除xml文件。打包完成后，打包线程反过来通知转换线程，转换线程继续转换。

**解决方案**

线程间的事件通知，可以使用标准库中Threading.Event:

1.等待事件一端调用wait，等待事件
2.通知事件一端调用set, 通知事件

## 8.4 如何使用线程本地数据

**实际案例**

我们实现了一个web视频监控服务器，服务器端采集摄像头数据，客户端使用浏览器通过http请求数据(观察服务器端采集到的画面)。我们通常使用的http请求都是短连接，服务端响应完之后就会关闭tcp连接。对于这里的需求就需要使用长连接，因为要持续不停的发送采集到的数据。
服务器端使用推送的方式(multipart/x-mixed-replace)一直使用一个tcp连接向客户端传递数据。这种方式将持续占用一个线程，导致单线程服务器无法处理多客户端请求。

改写程序，在每个线程中处理一个客户端请求，支持多客户端访问

**解决方案**

使用threading.local函数可以创建线程本地数据空间，其下属性对每个线程独立存在。


## 8.5 如何使用线程池

**实际案例**

之前实现了一个多线程web视频监控服务器，由于服务器资源有限(CPU,内存,带宽),需要对请求连接数(线程数)做限制，避免因资源耗尽而瘫痪。

可以使用线程池，替代原来的每次请求创建线程。