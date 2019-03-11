#!/bin/bash
# 演示 $* 和  $@
function print_params(){
	echo "\$1 = $1"
	echo "\$2 = $2"
	echo "\$3 = $3"
	echo "\$4 = $4"
}

function pass_params(){
	# $* 展开成一个从1开始的位置参数列表 （默认空格分割）
	# 在这里，就是将 "word" "word whth space" -> word word whit space
	echo -e "\n" '$* :'; print_params $*
	# "$*" 当加上双引号, 展开成一个位置参数  -> word word whth space（是一个整体）
	echo -e "\n" '"$*" :'; print_params "$*"
	# $@ 作用等同于 $*
	echo -e "\n" '$@ :'; print_params $@
	# "$@" 当加上双引号，将每一个位置参数展开成分开的字符串  -> word 和 word whth space（是2个）
	echo -e "\n" '"$@" :'; print_params "$@"
}

pass_params "word" "word whth space"