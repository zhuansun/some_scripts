#!/bin/bash
#参数展开实现大小写转换

# \${param,,} 把 param 的值全部展开成小写字母。
# \${param,} 仅把 param 的第一个字符展开成小写字母
# \${param^^} 把 param 的值全部展开成大写字母。
# \${param^} 仅把 param 的第一个字符展开成大写字母

# 我的mac不支持

if [[ $1 ]]; then
	echo ${1,,}
	echo ${1,}
	echo ${1^^}
	echo ${1^}
fi
