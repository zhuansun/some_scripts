#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'测试模块'

__author__='zs'

import sys

def test():
	args=sys.argv
	if len(args)==1:
		print("hello world1")
	elif len(args)==2:
		print("hello world2")
	else:
		print("hello world3")

if __name__=='__main__':
	test()



# 凡是使用_xxx开头的参数属于私有函数或变量。不可以被外部引用。 