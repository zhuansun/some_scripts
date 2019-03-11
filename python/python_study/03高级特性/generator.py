# 生成器
L=[x * x for x in range(10)]
print(L)

g=(x * x for x in range(10))
print(g)

print('---',next(g))
print('---',next(g))
print('---',next(g))
print('---',next(g))
print('---',next(g))
print('---',next(g))
print('---',next(g))
print('---',next(g))

for x in g:
	print(x)
