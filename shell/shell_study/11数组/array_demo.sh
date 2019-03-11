#!/bin/bash
# 计算文件修改次数的脚本

function usage(){
	echo "usage : ${basename $0} directory" >&2
}

# 检查参数是否是一个目录
if [[ ! -d $1 ]]; then
	usage
	exit -1
fi

# 初始化数组
for i in {0..23}; do
	hours[i]=0
done

# 收集数据
# stat -c %y "$1"/* 表示对用户用户的目录下的所有文件执行stat命令，并且使用-c格式化输出结果
# cut -c 12-13 表示对输出的结果进行截取。12-13位
# stat -c "%y" array_demo.sh --->  2019-02-15 16:14:57.711749015 -0500
# stat -c "%y" array_demo.sh | cut -c 12-13 --->  16
for i in $(stat -c %y "$1"/* | cut -c 12-13); do
	# i/#0 表示对08，09这样的数字，去除开头的0
	j=${i/#0} # j表示是当前文件的修改时间的小时数
	((++hours[j]))
	((++count))
done

# 展示数据
echo -e "Hour\tFiles"
echo -e "----\t-----"
for i in {0..23}; do
	printf "%02d\t%d\n" $i ${hours[i]}
done

printf "\nTotal files = %d\n" $count




