from collections import Iterable
# 怎么判断一个对象是否可迭代呢？
b = isinstance('abc', Iterable)
print(b)

c = isinstance([1,2,3], Iterable)
print(c)

d=isinstance(123, Iterable)
print(d)




