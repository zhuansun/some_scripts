from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print("运行子进程 %s (%s)" % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 30)
    end = time.time()
    print("子进程 %s 运行了 %0.2f 秒" % (name, (end - start)))

if __name__ == '__main__':
    print("父进程 %s " % (os.getpid()))

    # 限制同时运行几个进程
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print("等待所有的子进程运行结束")
    p.close()

    # 对Pool对象调用join()方法会等待所有子进程执行完毕
    p.join()
    print("所有的进程运行结束")