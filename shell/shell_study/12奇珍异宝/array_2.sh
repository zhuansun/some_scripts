#!/bin/bash
# 将使用组命令，看几个与关联数组结合使用的编程技巧。这个脚本， 称为array-2，当给定一个目录名，打印出目录中的文件列表，伴随着每个文件的文件所有者和 组所有者

declare -A files file_group file_owner group owners

if [[ ! -d "$1" ]]; then
	echo "参数不是个目录，参数错误" >&2
	echi 1
fi

for i in "$1"/*; do
	owner=$(stat -c %U "$i")
	group=$(stat -c %G "$i")
	files["$i"]=$i
	file_owner["$i"]=$owner
	((++owners[$owner]))
	((++groups[$group]))	
done

# 子shell相当于开启了一个新的线程，运行完毕后，线程自动关闭。




