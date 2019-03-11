#!/bin/bash
# 逻辑操作符(或 且 非)结合expression--->判断一个整数是否属于某一个范围内

# 有bug，不知道为啥？？？ 4比10大？？
MIN=10
MAX=100
INT=1
if [[ (($INT < $MIN)) ]]; then
	echo "$INT 比 $MIN 小"
elif [[ (($INT > $MAX)) ]]; then
	echo "$INT 比 $MAX 大"
fi
exit

