#!/bin/bash
# 多线程异步 father

echo "父线程: 开启..."
echo "父线程: 启动子线程..."
child &
pid=$!
echo "父线程: 子线程 (PID= $pid) 已启动."
echo "父线程: 继续运行..."
sleep 2
echo "父线程: 等待子线程完成..."
wait $pid
echo "父线程: 子线程完成,继续..."
echo "父线程: 父线程 结束，退出."