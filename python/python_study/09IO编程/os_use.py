
# 读取系统环境变量
import os
print(os.name)
print(os.environ.get("PATH"))


# 查看当前目录的绝对路径:
os.path.abspath('.')
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('/Users/michael', 'testdir')
# 然后创建一个目录:
os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
os.rmdir('/Users/michael/testdir')

# 拼接路径
os.path.join("","")

# 拆分路径
os.path.split("")


# 重命名文件
os.rename("","")
