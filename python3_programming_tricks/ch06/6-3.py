
from xml.etree import ElementTree

# 解析xml文件

et = ElementTree.parse('demo.xml')

# 从字符串中解析使用：ElementTree.fromstring

# 获取根元素

root = et.getroot()

# 根元素的属性与方法

root.tag
root.attrib

# 一个元素是一个可迭代对象，每次迭代出来的就是子元素
c1 = list(root)[0]
c1.attrib
c1.get('name')

year = list(c1)[1]

year.text
c1.text
year.tail
c1.tail

# 在一个元素下寻找其子元素中特定名称的元素

c1.find('neighbor') # 找第一个

# 找任意位置
list(root.iter('neighbor')) # 查找所有neighbor

# 找孙子节点下的name属性

list(root.iterfind('./*/*[@name]')) # xpath表达式

# 得到所有文本

list(c1.itertext())
' '.join(t for t in c1.itertext() if not t.isspace()) # join的参数是生成器




