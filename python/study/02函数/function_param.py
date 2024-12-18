# 函数的参数
# 除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

# 计算任意数的平方
def power(x):
	return x * x
print(power(2))

# 计算任意数的任意次方
def power_upper_1(x,n):
	sum=1
	while n>0:
		sum=sum*x
		n=n-1
	return sum
print(power_upper_1(2,2))

# 使用默认参数
def power_upper_2(x,n=2):
	sum=1
	while n>0:
		sum=sum*x
		n=n-1
	return sum
print(power_upper_2(3,1))

# 说是函数的默认参数必须指向不变对象！但是我这里测试的没问题啊
def power_error(L=[]):
	L.append('END')
	return L
print(power_error())
print(power_error([1,2,3]))


# 可变参数(tuple)
def sum_change(*number):
	sum=0
	for x in number:
		sum+=x
	return sum
print(sum_change(1,2,3,4,5))
# 如果已经有一个list或者tuple，怎么调用可变参数函数
number=[1,2,3,4,5]
print(sum_change(*number))


# 关键字参数(dict)
def sum_change_dict(name,age,**others):
	print('name: {0} ,age: {1} ,others: {2}'.format(name,age,others))
	return
sum_change_dict('zs',12)
sum_change_dict('zs',12,city='bj')
# 如果已经有个dict了，怎么调用函数
d={'city':'bj','job':'java'}
sum_change_dict('zs',12,**d)


# 限制关键字参数函数，对于这种函数，city和job就是必须要输入的参数
def stu_information(name,age,*,city,job):
	print(name,age,city,job)
	return
stu_information('张三',12,city='bj',job='java')

print("===========================================")

# 组合参数: 必选参数，默认参数，可变参数，命名关键字参数，关键字参数

def f1(a, b, c=0, *args, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
	return
def f2(a, b, c=0, *, d, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
	return
f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f2(1,2,d=4,x=99)

# 使用tuple和dict
args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args, **kw)






