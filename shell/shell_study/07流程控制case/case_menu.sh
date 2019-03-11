#!/bin/bash
# 使用cash语句实现目录
clear
cat <<- _EOF_
	请选择
	1->输出'你是狗'
	2->输出'你是2'
	3->输出'什么玩意'
	0->退出
_EOF_
read -p "请开始你的选择" INPUT
case $INPUT in
	1 ) echo "你是狗"
		;;
	2 ) echo "你是2"
		;;
	3 ) echo "什么玩意"
		;;
	0 ) echo "已退出"
		exit
		;;
	* ) echo "你看看你输入的是个什么玩意"
		;;
esac