#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'测试学生类'

# 学生类
'''
class Student(object):
	"""docstring for student"""
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		# print ("%s: %s" % (self.name, self.score))
		print ("{0}: {1}".format(self.name, self.score))
		return

lisi = Student('lsili',89)
lisi.print_score()
# 因为没有设置私有变量，所以可以直接访问变量，这样不好
lisi.name='zs'
lisi.print_score()
'''

'''
__以双下划线开头的是私有变量，不能在外部访问
'''

class Student(object):
	"""docstring for student"""
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def print_score(self):
		# print ("%s: %s" % (self.name, self.score))
		print ("{0}: {1}".format(self.__name, self.__score))
		return

lisi = Student('lsili',89)
lisi.print_score()
# 因为没有设置私有变量，所以可以直接访问变量，这样不好,使用__设置私有变量后，就可以啦
lisi.__name='zs'
lisi.print_score()


