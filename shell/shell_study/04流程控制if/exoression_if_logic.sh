#!/bin/bash
# 逻辑操作符(或 且 非)结合id--->判断一个整数是否属于某一个范围内
MIN=1
MAX=10
INT=4

if [[ $INT -lt $MIN ]]; then
	echo "$INT 比 $MIN 小"
elif [[ $INT -gt $MAX ]]; then
	echo "$INT 比 $MAX 大"
elif [[ $INT -gt $MIN && $INT -lt $MAX ]]; then
	echo "$INT 位于 $MIN 和 $MAX之间"
fi
exit
