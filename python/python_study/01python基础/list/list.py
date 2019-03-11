# list列表
classmates = ['张三','李四','王五','赵六']
print("claamates中的数据是：%s" % classmates)
print("claamates中的长度是：%d" % len(classmates))
print("我们也可以获取其中指定的某一个元素，比如0位元素: %s" % classmates[0])
print("我们也可以从后往前获取其中指定的某一个元素，比如-2位元素: %s" % classmates[-2])
print("也可以对该列表进行追加元素:list.append('xxx')")
classmates.append("郑七")
print("追加后的classmates: %s" % classmates)
print("也可以对该列表在指定位置添加元素:list.insert(1,'xxx')")
classmates.insert(1,"孙八")
print("添加后的classmates: %s" % classmates)
print("也可以对该列表进行末尾处删除:list.pop()")
classmates.pop()
print("删除后的classmates: %s" % classmates)
print("也可以对该列表中的某个元素进行替换:classmates[1]='xxx'")
classmates[1] = '尹九'
print("替换后的classmates: %s" % classmates)
print("一个list中的元素类型可以是不同的,比如我添加一个整形和一个boolean型进去")
classmates.append(1234)
classmates.append(True)
print("添加后的classmates",classmates)
print("一个lisi中除了元素类型不同外，还可以嵌套数组")
newClass=['new1','new2']
print("比如这是一个新的数组newCalls",newClass)
print("追加到之前的classmates中")
classmates.append(newClass)
print("添加后的classmates",classmates)

