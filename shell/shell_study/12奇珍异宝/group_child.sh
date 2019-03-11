#!/bin/bash
#组命令和子shell


# 组命令 大括号，命令和括号之间有空格: { command1; command2; [command3;...] }

# 子shell 小括号  : (command1;command2,[command3;...])

# 实现将三个命令的输出结果，输出到同一个文件中

# 传统写法
ls -l > foo.txt
echo "this is test" >> foo.txt
cat foo_test.txt >> foo.txt

# 使用组命令
{ ls -l; echo "this is test"; cat foo_test.txt } > foo.txt

# 使用子shell
(ls -l; echo "this is test"; cat foo_test.txt) > foo.txt


# 与管道线结合使用
{ ls -l; echo "this is test"; cat foo_test.txt } | lpr


