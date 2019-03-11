# type()用于判断对象的类型
'''
class Student(object):
	pass

student = Student()
print(type(student))
print(type(123))
'''

# types用于判断方法的类型
'''
import types

def fun1():
	print("hello world")
	return

if type(fun1) == types.FunctionType:
	print(True)
'''

# isinstance() 就很高级了
'''
- 判断对象类型
- 判断方法类型
- 判断某一个变量是否属于某一类


print("1-->",isinstance(123,int))
print("2-->",isinstance(123,str))
print("3-->",isinstance([1,2,3],(list,tuple)))
print("4-->",isinstance([1,2,3],(list,tuple)))

class Student(object):
	pass
student = Student()

print("5-->",isinstance(student,Student))


import types
def funq():
	pass
print("6-->",isinstance(funq,types.FunctionType
'''

# dir() 获取一个对象的所有属性和方法
'''
class Student(object):
	"""docstring for Student"""
	def __init__(self, __name,__score):
		self.__name = __name;
		self.__score = __score;
	def sayHello():
		print("hello world")
		return
	def readBook():
		print("read book")
		return
	def readSomething(self,str):
		print("%s what to say: %s" % (self.__name,str))
		return	
	def __len__(self):
		return 2
student = Student("张三","98")
print(dir(student))
print(len(student))
print()
# 不能获取隐藏属性
print("有属性__name吗？",hasattr(student,'__name'))
print("设置属性name！",setattr(student,'name',"王五"))
fn = getattr(student,'readSomething')
fn("fuck you")
'''


# 实例属性和雷属性
'''
>>> class Student(object):
...     name = 'Student'
...
>>> s = Student() # 创建实例s
>>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
Student
>>> print(Student.name) # 打印类的name属性
Student
>>> s.name = 'Michael' # 给实例绑定name属性
>>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
Michael
>>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
Student
>>> del s.name # 如果删除实例的name属性
>>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
Student
'''



