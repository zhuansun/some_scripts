#!/bin/bash
# 使用while读取文件 ：使用重定向操作符将文本中的内容输入到while循环中
while read distros version release; do
	printf "Distros: %s\tVersion: %s\tRelease: %s\n" \
		$distros \
		$version \
		$release
done < distros.txt