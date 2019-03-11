#!/bin/bash
# 表达式 id 整形,使用算数符合指令,可以略为简化使用-lt -gt -eq 等命令
# 在 (()) 里可以不使用$展开符


# 有bug，不知道为啥？？？ -1是整数？？？？

INT=-2
if [[ $INT =~ ^-?[0-9]+$ ]]; then
	if [[ -z "$INT" ]]; then
		echo "INT 为空" >&2
		exit 1
	fi
	if [[ ((INT == 0)) ]]; then
		echo "$INT 为 0"
	else
		if [[ ((INT > 0)) ]]; then
			echo "$INT 是正数"
		else
			echo "$INT 是负数"
		fi
		if [[ $((INT % 2)) -eq 0 ]]; then
			echo "$INT 是2的整数倍"
		else
			echo "$INT 不是2的整数倍"
		fi
	fi
else
	echo "$INT 不是整数"
fi
exit