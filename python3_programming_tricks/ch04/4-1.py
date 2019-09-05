
# 先导入可迭代对象基类和迭代器对象基类
from collections import Iterable, Iterator

"""
for 循环内部工作流程：
l = [1,2,3,4,5]
for x in l:
    print(x)

for循环中，in后面的必须是可迭代对象：
isinstance(l, Iterable) # 返回True, l是可迭代对象
issubclass(list, Iterable) # 返回True,列表list是可迭代对象
iter(l) # 返回迭代器对象
l.__iter__()
Iterable.__abstractmethods__
it = iter(l)
next(it) # next调用的是it.__next__()方法

for循环流程:
    1 调用iter(),将l传入，得到可迭代对象it
    2 使用next(it)进行迭代，循环迭代
    3 直到抛出StopIteration异常，循环就结束了

迭代器对象是一次性消费，消费完成后就没有了。要想在迭代，需要重新
创建迭代器，且两个不同的迭代器是不相互干扰的

"""

# 如何获得一个城市的气温

# url = 'http://wthrcdn.etouch.cn/weather_mini?city=北京'
url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + '北京'
import requests
r = requests.get(url)
r.text # 返回字符串
r.json() # 返回Python字典
r.json()['city'] # 返回：北京
r.json()['data']['forecast'][0] # 第0项是今天的温度，第1项是明天的温度

# the following is the solution code

from collections import Iterable, Iterator


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)

    def get_weather(self, city):
        url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city
        r = requests.get(url)
        data = r.json()['data']['forecast'][0]
        return city, data['high'], data['low']


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


def show(w):
    for x in w:
        print(x)

w = WeathIterable(['北京','上海','广州'] * 10)
show(w)
