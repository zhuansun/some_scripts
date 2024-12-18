import itertools

# 创建一个无限循环的集合
natuals = itertools.count(1)
# for n in natuals:
#    print(n)

# 把一个集合无限循环
cycle = itertools.cycle('ABC')
# for c in cycle:
#    print(c)


# 对某个元素 无限循环(不限制后面的数字，就是无限循环)
ns = itertools.repeat('A',4)
for n in ns:
    print(n)


# chain()  groupBy()