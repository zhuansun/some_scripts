#!/bin/bash
# 简单的使用if进行判断,使用 expression模式 高级篇 判断文件

FILE=~/java_error_in_datagrip.hprof
# -e 判断是否存在
if [[ -e "$FILE" ]]; then
	# -f 判断是否是文件
	if [[ -f "$FILE" ]]; then
		echo "$FILE 是一个合法文件"
	fi
	# -d 判断是否是目录
	if [[ -d "$FILE" ]]; then
		echo "$FILE 是一个目录"
	fi
	# -r 文件是否可读
	if [[ -r "$FILE" ]]; then
		echo "$FILE 可读"
	fi
	# -w 文件是否可写
	if [[ -w "$FILE" ]]; then
		echo "$FILE 可写"
	fi
	# -x 文件是否可执行
	if [[ -x "$FILE" ]]; then
		echo "$FILE 可执行"
	fi
else
	echo "$FILE 不存在"
	exit 1
fi
exit