#!/bin/bash
# 大小写转换， bash有四个参数展开和delare的两个选项来支持大小写转换【我的mac不支持啊】

declare -u upper
declare -l lower
if [[ $1 ]]; then
	upper="$1"
	lower="$1"
	echo $upper
	echo $lower
fi