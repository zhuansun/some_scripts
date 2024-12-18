# 迭代，迭代除了可以使用循环之外，还可以使用 for .. in  类似于，Java中增强的for循环

d={'a':1,'b':2,'c':3}

# 默认迭代的是key
for x in d:
	print(x)

# 如果要迭代value
for x in d.values():
	print(x)

# 如果要迭代每一个元素
for x in d.items():
	print(x)



