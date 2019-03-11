#/bin/bash
# 通过函数，了解什么是局部变量

# 设置一个全局变量
foo=0
function func_1(){
	# 函数func_1中的局部变量
	local foo
	foo=1
	echo "func_1 : foo = $foo"
}

function func_2(){
	local foo
	foo=2
	echo "func_2 : foo = $foo"
}

echo "global : foo = $foo"

func_1

echo "global : foo = $foo"

func_2

echo "global : foo = $foo"
