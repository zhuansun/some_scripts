# 使用生成器生成杨辉三角

'''我的垃圾代码

def triangle(n):
	if not isinstance(n,int):
		raise TypeError("错误的参数调用")
	for currentline in range(1,n):
		line=[x for x in range(currentline)]
		yield line
	return

for x in triangle(3):
	print(x)
'''


''' 大神的方法1
def triangle():
	j=0
	L=[]
	while True:
	    s=[1 for x in range(len(L))] #此处产生一个元素个数与L相同的列表，且头元素为1，以便迭代产生下一个列表
	    for i in range(j-1):
	        s[i+1]=L[i]+L[i+1] #此处用s迭代产生下一个列表
	    s.append(1)
	    L=s
	    yield L
	    j=j+1
	return 'done'

for x in triangle():
	print(x)
'''


''' 大神的方法二
j = 0
    L = []
    while True:
        s=L[:]
        for i in range(j-1):
            L[i+1]=s[i]+s[i+1]
        L.append(1)
        yield L
        j=j+1
    return 'done'
'''

def triangle():
	L = [1]
	while True:
		yield L
		L = [x+y for k,x in enumerate([0]+L) for j,y in enumerate(L+[0]) if k==j]
	return L

for x in triangle():
	print(x)









