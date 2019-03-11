'''
f = open("文件路径","读写方式","编码","对读取的错误处理方式")
文件路径：完整的文件路径
读写方式：
    r : 默认读文本
    rb : 读取二进制
    w : 写(文件已存在，默认覆盖文件)
    wa : 追加写文件
编码：
    默认：UTF-8
    指定编码：encoding='gbk'
对读取的错误处理方式：
    errors='ignore'

'''



import logging
logging.basicConfig(level=logging.INFO)

# 读文件
# try:
#     f = open("/Users/zhuansunpengcheng/yuntu/workspace_python/workspace/python/09IO编程/file.txt","r")
#     print(f.read())
# finally:
#     logging.info("close file")
#     if f:
#         f.close()


# 简化的读文件操作
with open("/Users/zhuansunpengcheng/yuntu/workspace_python/workspace/python/09IO编程/file.txt","r") as f:
    print(f.read())

# 几种读取文件的方式
'''
    1.read() 一次全读取完，放在内存中
    2.read(size) 一次读取size字节的内容
    3.readline() 每次读取一行
    4.readlines() 一次去读取完
'''


# 读取图片，视频等二进制文件
f = open("xxx.jpg","rb")
f.read()


# 指定字符编码

f = open("xxx",encoding="gbk",errors="ignore")

# 写文件
f = open("xxx","w")
# 可以多次写
for i in range(101):
    f.write("hello world")
# 但是要记得关闭
f.close()




