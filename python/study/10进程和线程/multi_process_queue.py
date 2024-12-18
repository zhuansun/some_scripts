from multiprocessing import Process, Queue
import os, time, random

def write(q):
    for value in ['A',"B",'C','D']:
        print('把 %s 放进去了' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    while True:
        print("把 %s 取出来了" % q.get())

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    # 如果不关掉，就相当于是一直监听，，，
    pr.terminate()