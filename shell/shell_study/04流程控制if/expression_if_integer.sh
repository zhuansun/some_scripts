#!/bin/bash
# 表达式 id 整形
INT=3
if [[ $INT =~ ^-?[0-9]+$ ]]; then
	if [[ -z "$INT" ]]; then
		echo "INT 为空" >&2
		exit 1
	fi
	if [[ $INT -eq 0 ]]; then
		echo "$INT 为 0"
	else
		if [[ $INT -gt 0 ]]; then
			echo "$INT 是正数"
		elif [[ $INT -lt 0 ]]; then
			echo "$INT 是负数"
		fi
		if [[ $(($INT % 2)) -eq 0 ]]; then
			echo "$INT 是2的整数倍"
		else
			echo "$INT 不是2的整数倍"
		fi
	fi
else
	echo "$INT 不是整数"
fi
exit