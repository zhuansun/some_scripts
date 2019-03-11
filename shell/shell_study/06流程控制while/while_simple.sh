#!/bin/bash
# while循环的简单实用
count=1
while [[ $count -le 5 ]]; do
	echo $count
	count=$((count + 1))
done
echo "完成"