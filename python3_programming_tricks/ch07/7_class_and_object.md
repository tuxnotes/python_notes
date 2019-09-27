
# 7 类与对相关相关话题

## 7.1 如何派生内置不可变类型并修改其实例化行为

**实际案例**

比如我们想自定义一种新类型的元组，对于传入的可迭代对象，我们只保留其中int类型且值大于0的元素，例如：

IntTuple([1, -1, 'abc', 6, ['x','y'],3]) => (1,6,3)

如何继承内置tuple实现IntTuple?


**解决方案**

继承内置tuple,并实现\_\_new\_\_.在其中修改实例化行为