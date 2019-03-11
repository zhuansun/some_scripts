# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

# 1.tuple 定义
a = (1,2)

# 1.tuple 定义空元素
b = ()

# 定义只有一个元素的tuple,必须加一个,消除歧义
c = (1,)

# 可变的tuple,tuple不可变，可变的是其中的list
d = ('a','b',['A',"B"])
d[2][0] = 'X'
d[2][1] = 'Y'




# list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。