# 定制类
'''
所有以__xxx__形式命名的函数，都是一些特殊函数
'''

# __str__
class Student(object):
	pass
student = Student()
# 默认输出: <__main__.Student object at 0x1036a5a90>
print(student)


class Teacher(object):
	def __init__(self, __name):
		self.__name = __name
		return
	def __str__(self):
		return "这是Teacher类的一个示例，名字是：{0}".format(self.__name)
teacher = Teacher("孙老师")
print(teacher)

			
# __repr__ 返回程序开发者看到的字符串

class People(object):
	def __init__(self, __name):
		self.__name = __name
		return
	def __str__(self):
		return "这是People类的一个示例，名字是：{0}".format(self.__name)
	__repr__ = __str__
		


# __iter__
'''
如果一个类想被 for..in..进行循环。就必须实现这个方法，该方法返回一个可被迭代的对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
'''
class Fib(object):
	"""docstring for Fib"""
	def __init__(self):
		self.a, self.b = 0,1
		return
	def __iter__(self):
		return self
	def __next__(self):
		self.a, self.b = self.b, self.a+self.b
		if self.a > 1000:
			raise StopIteration()
		return self.a

for x in Fib():
	print(x)


# __getitem__ 用于根据下标获取元素
class Fib2(object):
	def __getitem__(self,n):
		a, b = 1,1
		for x in range(n):
			a, b = b, a+b
		return a

f = Fib2()
print(f[100])



# __getattr__ 对不存在的参数，发返回默认值
class Animal(object):
	def __init__(self, __name):
		self.__name = __name;
		return
	def __getattr__(self, value):
		if value == 'age':
			return 22
		return 11
a = Animal("moouse")
# 因为__name是私有属性，所以找不到，默认返回 11
print(a.__name)
print(a.age)
print(a.mls)



# __call__ 
'''
一般情况下，我们都是用类，创建对象，然后通过对象.方法()的形式调用方法
那么能不能用对象本身，直接调用呢？ 
'''
class Cat(object):
	def __init__(self, __name):
		self.__name = __name
		return
	def __call__(self):
		return "这只猫的名字是:{0}".format(self.__name)

cat = Cat("tom")
print(cat())

# 判断一个对象是否可以直接调用,使用 callable
print(callable(cat))




















