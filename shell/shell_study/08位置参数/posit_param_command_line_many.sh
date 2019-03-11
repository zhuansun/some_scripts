#/bin/bash
# 当命令行接收大量的参数之后，怎么展示
# 什么意思呢？就是加入我们只有 $0-$5 但是我们的命令行参数有10个，可是我们只能展示5个？剩下五个怎么办？
count=1
while [[ $# -gt 0 ]]; do
	echo "参数 $count = $1"
	count=$((count++))
	shift
done

