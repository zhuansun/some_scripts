import time,threading,random

def loop():
    print("----->子线程 %s 正在运行中....." % (threading.current_thread().name))
    n = 0
    while n < 5 :
        n = n + 1
        print("----------->子线程 %s 打印出 %s " % (threading.current_thread().name,n))
        time.sleep(random.random())
    print("----->子线程 %s 运行结束" % (threading.current_thread().name))



if __name__ == '__main__':
    print("主线程 %s 正在运行中....." % (threading.current_thread().name))
    t = threading.Thread(target=loop,name='LoopThread')
    t.start()
    t.join()
    print("主线程 %s 运行结束" % (threading.current_thread().name))
