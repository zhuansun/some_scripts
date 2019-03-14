import asyncio

'''
这个多简单，去他妈的什么上一节吧。。这才是正常人类该用的
'''

async def hello():
    print("程序首先打印出一个 hello world")
    r = await asyncio.sleep(1)
    print("hello again!")


async def hello2():
    print("线程并不会等待，继续执行下一个")



loop = asyncio.get_event_loop()
tasks = [hello(), hello2()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


'''
把@asyncio.coroutine替换为async；
把yield from替换为await。
'''
