# 切片： 类似java语言中的substring

# 生成一个list，0-100
L=list(range(100))
print(L)


# 取出前十个
print(L[:10])

# 取出后十个
print(L[-10:])


# 11-20个
print(L[10:20])

# 前十个数，每隔2个取一个
print(L[:10:2])

# 所有的数，每隔5个取一个
print(L[::5])
