#!/bin/bash
# 展示菜单，读取用户的选择的菜单，并进行输出


function input_invalid(){
	echo " $INPUT 非法 "
	exit 1
}

read -p "请选择
1->输出'你是狗'
2->输入'你是2'
3->输入'什么玩意' >" INPUT

[[ -z $INPUT ]] && input_invalid

(( $(echo $PARAM | wc -w) >1 )) && invalid_input

if [[ (($INPUT == 1)) ]]; then
	echo "你是狗"
elif [[ (($INPUT == 2)) ]]; then
	echo "你是2"
elif [[ (($INPUT == 3)) ]]; then
	echo "什么玩意"
else
	echo "你看看你输入的是个什么玩意"
	exit 1
fi
exit
