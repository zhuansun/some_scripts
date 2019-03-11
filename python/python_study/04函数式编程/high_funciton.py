# 高阶函数


# map
'''
map将传入的函数，依次作用于序列中的每个元素
'''
def doublex(x):
	return x**2
# print(list(map(doublex,[1,2,3,4,5])))

# print(list(map(str,[1,2,3,4,5])))

# reduce
'''
reduce把一个函数(该函数必须接受两个参数)作用在一个序列[x1, x2, x3, ...]上，reduce把结果继续和序列的下一个元素做累积计算
'''
from functools import reduce
def add(x,y):
	return x+y
# print(reduce(add,[1,2,3,4,5]))


# map结合reduce将一个str '198372' 转成int
def str2int(x):
	d={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
	return d[x]
def fn(x,y):
	return x*10+y;
# print(reduce(fn,map(str2int,['1','2','3'])))


# lambda 函数
def str2int(x):
	d={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
	return d[x]
# print(reduce(lambda x,y: x*10+y,map(str2int,['1','2','3'])))


# filter
'''
用于对序列进行过滤
'''
def filter1(n):
	return not n%2==0
a=[1,2,3,4,5,6,7,8,9]
# print(list(filter(filter1,a)))


# sored排序，可以接受关键字参数


# 同时，高级函数可以将函数作为参数，也可以将函数作为返回值。

def fn1():
	# fn1里面定一个了一个list
	a=[]
	pass


# 装饰器


# 偏函数
'''
当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

'''














