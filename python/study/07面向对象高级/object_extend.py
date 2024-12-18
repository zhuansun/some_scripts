class People(object):
	pass

class Man(object):
	pass

class Student(People,Man):
	pass

# 学生既是人， 又是男人

'''
为了避免复杂的继承关系， 对于某些功能，可以抽象出来。 xxxMixIn
'''

		