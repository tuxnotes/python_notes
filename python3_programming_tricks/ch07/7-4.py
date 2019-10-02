class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        """访问器"""
        # 保留两位小数，且进行四舍五入
        return round(self.redius, 2) # 用户输入不变，内部决定保留几位

    def set_radius(self, radius):
        """定义设置器方法"""
        if not isinstance(radius, (int,float)):
            raise TypeError("wrong type")
        self.radius = radius

    @property # 装饰器方式
    def get_area(self):
        return sefl.radius ** 2 * math.pi
    @S.setter
    def set_area(self, S):
        self.radius = math.sqrt(S / math.pi)

    R = property(get_radius, set_radius) # 使用函数方法

c = Circle(5.712)
c.S = 99.88
print(c.S)
print(c.R)
