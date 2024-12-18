import os

# 当前进程的pid
cid = os.getpid()

print("程序开始运行: %s" % cid)

pid2 = os.fork()

if pid2 == 0:
    print("我是子进程 (%s)，我的父进程是 (%s)" % (os.getpid(), os.getppid()))
else:
    print("我是父进程 (%s), 我刚创建了一个子进程 (%s)" % (cid,pid2))