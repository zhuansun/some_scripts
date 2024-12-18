from multiprocessing import Process
import os
def run_proc(name):
    print("运行子进程 %s (%s)..." % (name, os.getpid()))

if __name__ == '__main__':
    # 程序入口
    print("父进程 %s " % os.getpid())
    # 开始创建一个子进程
    p = Process(target=run_proc, args=('test',))

    print('子进程即将开始')
    # 开启子进程
    p.start()
    # 子进程结束后，继续运行
    p.join()

    print("子进程结束")

