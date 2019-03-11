# 序列化对象
import pickle,os
# 创建一个对象
d = dict(name='bob',age=20,score=80)
# 获取当前目录
path = os.path.abspath('.')
# 创建文件
fpath = os.path.join(path,"pico.txt")
f = open(fpath,'wb')
print(f)
# 序列化保存(用的方式dump() dumps()是直接序列化一个对象)
# pickle.dumps(d, f) 这个是错的，一开始找了好久，没想到多了一个s
pickle.dump(d, f)
# 关闭文件
f.close()



# 反序列化
f = open(fpath,"rb")
d = pickle.load(f)
f.close()
print(d)