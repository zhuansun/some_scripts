#!/bin/bash
# 读取键盘输入的整数，判断是否大于10
echo "请输入一个整数"
read INT
if [[ $INT =~ ^-?[0-9]+$ ]]; then
	echo "$INT 是一个整数"
else
	echo "$INT 不是数字啊"
fi
exit