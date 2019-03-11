#!/bin/bash
# 数组的基本语法

# 什么是数组
a[1]=foo
echo ${a[1]}

# 数组的声明 使用 -a
declare -a arr

# 数组的赋值
# 单个赋值
arr[0]=arr0
arr[1]=arr1
for (( i = 0; i < 2; i++ )); do
	echo ${arr[i]}
done

# 多个赋值
arr=(arr00 arr11 arr22)
for (( i = 0; i < 3; i++ )); do
	echo ${arr[i]}
done


# 查看数组的长度 
echo ${#arr[@]}

#(shell中的数组长度，是指有值的元素个数，并不等同于其他语言中的数组长度),如下，输出结果是1
leng[100]=foo
echo ${#leng[@]}


# 遍历数组下标和值
foo=([2]=a [4]=b [8]=c)
for i in "${foo[@]}"; do
	echo $i
done

for i in "${!foo[@]}"; do
	echo $i
done



#在数组尾部添加元素
foo=(a b c)
for i in ${foo[@]}; do
	echo $i
done
foo+=(d e f)
for i in ${foo[@]}; do
	echo $i
done


# 数组排序
echo "------------数组排序"
foo=(3 5 2 9 6)
echo "${foo[@]}"
sorted=($(for i in ${foo[@]}; do
	echo $i
done | sort))
echo "${sorted[@]}"



# 删除数组元素
echo "------------删除数组元素"
foo=(1 2 3 4 5 6)
echo ${foo[@]}
unset foo[0]
echo ${foo[@]}
unset foo
echo ${foo[@]}


# 创建关联数组
echo "---------创建关联数组"
declare -A colors
colors["red"]="#ff0000"
colors["green"]="#00ff00"
colors["blue"]="#0000ff"
echo ${colors["blue"]}








