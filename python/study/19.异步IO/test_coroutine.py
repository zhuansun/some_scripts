

# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator（生成器）
# 最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
# send(param) 方法是生成器自带的方法，该方法有一个参数，该参数指定的是上一次被挂起的yield语句的返回值
# 这么说，很难理解。我们参考下面的程序

# 从main开始
# 先是通过consumer这个生成器，生成了一个c： c = consumer() 
# 然后将这个生成器对象传给了生产者
# 生产者拿到c，先是 c.send(None) ，表示执行一次consumer
# consumer开始执行，遇到 n = yield r 开始暂停，并返回 r 
# 返回 r 给 producer，但是producer没有接收，所以略过，producer继续往下执行
# 执行 n = 0 , while n < 5 : n = n+ 1 prin.....当当当当，，执行到 r = c.send(n)的时候
# 这个时候又调用了consumer ，但是因为consumer是一个生成器，所以从上次暂停的地方开始执行，也就是 n = yield r
# 对于 n = yield r 来说，r = c.send(n) 表示将参数 n 赋值给 n = yield r 左边的n
# 然后 consumer 拿到 n 的值之后， 继续往下执行，会再次运行到 n = yield r 这句
# 之后就是将 n = yield r 右边的r返回， consumer再次暂停， 返回给谁呢？给 r = c.send(n) 左边的 r 
# 然后producer这次有r接收，所以在producer里面，r就拿到了consumer里的返回值，然后继续往下运行。
# 循环往复


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


