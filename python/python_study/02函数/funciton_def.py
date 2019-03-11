
# 函数的定义
def my_abs(x):
	if x>=0:
		return x
	else:
		return -x
print(my_abs(-23))

def my_abs_exception(x):
	if not isinstance(x,(int,float)):
		raise TypeError('错误的输入类型')
	if x>=0:
		return x
	else:
		return -x
# print(my_abs_exception('a'))
print(my_abs_exception(3))

def my_fun(x):
	return x,x+1
a,b=my_fun(2)
print(a)
print(b)



