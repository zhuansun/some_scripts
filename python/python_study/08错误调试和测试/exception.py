# 日志捕获
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
        # print("哈哈哈")
    finally:
        print("我去你吗的")

# main()
# print('END')



# 异常抛出

# 我把我的错误信息，返回到上层
def foo1(s):
    try:
        return 10 / int(s)
    except Exception as e:
        raise

# 我是上层，我把错误信息给吃了
def bar1(s):
    try:
        return foo1(s) * 2
    except Exception as e:
        print("异常被我吃了")

bar1("0")
print('END')
