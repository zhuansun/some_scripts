#!/bin/bash
# 展示菜单，读取用户的选择的菜单，并进行输出
while [[ $INPUT != 0 ]]; do
	cat <<- _EOF_
		请选择
		1->输出'你是狗'
		2->输入'你是2'
		3->输入'什么玩意'
	_EOF_

	read -p "请输入你的选择" INPUT

	if [[ (($INPUT == 1)) ]]; then
		echo "你是狗"
	elif [[ (($INPUT == 2)) ]]; then
		echo "你是2"
	elif [[ (($INPUT == 3)) ]]; then
		echo "什么玩意"
	else
		echo "你看看你输入的是个什么玩意"
	fi

done
echo "拜了个拜"
exit
