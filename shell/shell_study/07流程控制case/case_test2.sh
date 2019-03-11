#!/bin/bash
# 测试用例，;;& 表示找到匹配记过后，继续往下运行(;;&)这个符号部分机器不适配
# 我用的mac电脑就不支持，但是在centos7中就是可以的

read -p "请开始你的输入" INPUT
case $INPUT in
	# 匹配模式
	[[:alpha:]] ) echo "你输入的是一个字母"
		;;&
	[ABC][0-9] ) echo "你输入的是大写字母后紧跟着一个数字"
		;;&
	??? ) echo "你输入的是一个三位的字符串"
		;;&
	*.txt ) echo "你输入的是以.txt结尾的字符串"
		;;&
	# 逻辑匹配
	a|A ) echo "你输入的是a/A"
		;;&
	zhuan|yin ) echo "你输入的是zhuan/yin"
		;;&

	#通用匹配
	* ) echo "你输入的是啥，自己心里没点逼数吗？"
		;;&
esac