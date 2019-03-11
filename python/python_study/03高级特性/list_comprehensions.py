# 列表生成式

# 生成列表的方式一，利用for循环
L1=[]
for x in range(10):
	L1.append(x)
print(L1)


# 生成列表的方式二，利用list()函数
L2=list(range(10))
print(L2)

# 生成列表的方式三，高级，推荐，使用列表生成shi
L3=[x*x for x in range(1,11)]
print(L3)

L4=[x for x in range(10)]
print(L4)

L5=[x for x in range(10) if x%2==0]
print(L5)

L6=[x+y for x in ('A','B','C') for y in ('X','Y','Z')]
print(L6)