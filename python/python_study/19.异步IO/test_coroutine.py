

# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator（生成器）
# 最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def consumer() :
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[消费者] 消费了 %s' % n)
        r = '200 OK'


def producer(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[生产者] 生产了 %s ' % n)
        r = c.send(n)
        print('[消费者] 消费者返回了 %s ' % r)
    c.close()

if __name__ == '__main__':
    c = consumer()
    producer(c)


