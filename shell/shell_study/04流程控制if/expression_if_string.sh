#!/bin/bash
# 使用表达式进行字符串的if比较
ANSWER="maybe"
# 字符串的长度为0
if [[ -z "$ANSWER" ]]; then
	echo "没有输入答案" >&2
	exit 1
fi

if [[ "$ANSWER" == "yes" ]]; then
	echo "答案是 YES"
elif [[ "$ANSWER" == "no" ]]; then
	echo "答案是 NO"
elif [[ "$ANSWER" == "maybe" ]]; then
	echo "答案是 MAYBE"
else
	echo "没有输入答案";
fi
exit