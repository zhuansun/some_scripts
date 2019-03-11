class Student(object):
	def getName(self):
		return self.name
	def setName(self,name):
		self.name = name
		return

student = Student()
student.setName("lisi")
print(student.getName())


# @property 是把一个方法变成属性，可以直接通过属性直接调用
class Teacher(object):
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self,name):
		self._name = name
		return
t = Teacher()
t.name='zs'
print(t.name)	

# 必须要加上_ ，要不然会报错
class Teacher1(object):
	@property
	def name(self):
		return self.name
	@name.setter
	def name(self,name):
		self.name = name
		return
t = Teacher1()
t.name='zs'
print(t.name)	

