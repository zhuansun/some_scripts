import threading

balance = 0
lock = threading.Lock()

def change_if(value):
    global balance
    balance = balance + value
    balance = balance - value


def run_thread(value):
    for i in range(1000000):
        lock.acquire()
        try:
            change_if(value)
        finally:
            lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=run_thread,args=(5,))
    t2 = threading.Thread(target=run_thread,args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)


