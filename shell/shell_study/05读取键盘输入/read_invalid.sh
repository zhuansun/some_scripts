#!/bin/bash
# 校正输入

function invalid_input () {
    echo "Invalid input '$PARAM'" >&2
	exit 1 
}

read -p "请输入一个字母 > " PARAM
# -z 判断变量的值是否为空 
[[ -z $PARAM ]] && invalid_input

(( $(echo $PARAM | wc -w) >1 )) && invalid_input

if [[ $PARAM =~ ^[-[:alnum:]\._]+$ ]]; then
	echo "'$PARAM' 是一个合法的名字"
	if [[ -e $PARAM ]]; then
		echo "'$PARAM' 文件已存在"
	else
		echo "'$PARAM' 文件不存在"
	fi
	# is input a floating point number?
    if [[ $PARAM =~ ^-?[[:digit:]]*\.[[:digit:]]+$ ]]; then
        echo "'$PARAM' 是一个浮点型."
    else
        echo "'$PARAM' 不是浮点型."
    fi
    # is input an integer?
    if [[ $PARAM =~ ^-?[[:digit:]]+$ ]]; then
        echo "'$PARAM' 是一个整形."
    else
        echo "'$PARAM' 不是一个整形."
    fi
fi