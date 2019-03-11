# 类实例的属性绑定
class Student(object):
	"""docstring for Student"""
	def __init__(self, __name):
		self.__name = __name
	def sayHello(self):
		print("{0} say hello world".format(self.__name))
		return

student = Student("张三")
student.sayHello()

# 对已经创建好的实例，绑定一个__score变量
student.__score=89
print(student.__score)

# 对已经创建好的实例，绑定一个方法
def readBook(self,bookName):
	self.bookName=bookName
	return
from types import MethodType
student.readBook = MethodType(readBook,student)
student.readBook("java")
print(student.bookName)


# 但是绑定的方法，只是对哪一个对象实例生效
'''
student2 = Student("王五")
student2.readBook("python")
print(student2.readBook)
'''

# 如果需要对所有的实例都生效，可以将方法绑定在类上
def setScore(self,score):
	self.score = score
	return
Student.setScore = setScore
student3 = Student("李四")
student3.setScore("89")
student3.sayHello()
print(student3.score)

'''
通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。
'''

# 限制对类绑定属性
class Teacher(object):
	__slots__ = ('name','age')
	def __init__(self, name):
		self.name=name
		
t = Teacher("赵六")
# 会报错
# t.score=3
# 可以正常绑定
t.age=3
print(t.age)

'''
__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
'''
class STeacher(Teacher):
	pass
st = STeacher("哈哈,继承的")
st.score=2222222
print(st.score)
		
'''
如果子类也添加了__slots__，name子类能使用的就是 父类的+当前定义的
'''
class STTeacher(Teacher):
	__slots__=('sex')
	pass
stt = STTeacher("哈哈,继承的")
stt.age=33333
print(stt.age)
stt.score=33333

'''
STTeacher 类只允许绑定， name,age.sex 其他的都不允许。 如果子类不限制__slots__，name所有的都可以绑定
'''




























