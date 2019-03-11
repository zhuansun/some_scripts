#!/bin/bash
# 接口键盘输入的数字，如果用户在 [一定时间] 内，没有输入任何东西，则程序退出。

if read -t 10 -p "请在十秒内输入一个数字 > " INT ;then
	if [[ $INT =~ ^-?[0-9]+$ ]]; then
		echo "$INT 是个数字"
	else
		echo "$INT 不是数字"
	fi
else
	echo "您没有输入任何信息"
	exit 1
fi


