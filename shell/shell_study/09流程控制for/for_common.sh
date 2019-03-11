#!/bin/bash
# shell的传统for循环
for (( i = 0; i < 10; i++ )); do
	echo $i
done


# 增强形式吧
for j in {A..D}; do
	echo $j
done