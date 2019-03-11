#!/bin/bash
# 使用while循环读取文件 ： 使用管道线将读取的内容输入到while循环中
sort -k 1,1 -k 2n distros.txt | while read distros version release; do
	printf "Distros: %s\tVersion: %s\tRelease: %s\n" \
		$distros \
		$version \
		$release
done