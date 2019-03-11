#!/bin/bash
# 子命令的进程替换

# 考虑下面的例子，read读取管道线的数据，赋值给REPLY，然后输出reply
# 我们预想的是 会在屏幕输出 foo， 但是结果是 空。

echo "foo" | read
echo $REPLY


# 为什么呢？因为read命令是在一个子shell中运行的。当read命令运行完之后，改子shell就全部销毁。不保留任何数据


# <(...)  使用这种进行进程替换就可以啦
# 进程替换允许我们把一个子 shell 的输出结果当作一个用于重定向的普通文件

read < <(echo "foo")
echo $REPLY
