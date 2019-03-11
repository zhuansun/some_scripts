#!/bin/bash
# 简单的使用if进行判断,使用 test 模式，但是更流行的是expression模式

x=5
if test $x = 5 ; then
	echo "x 等于 5"
else
	echo "x 不等于 5"
fi