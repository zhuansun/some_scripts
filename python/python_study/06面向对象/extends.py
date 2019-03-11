
class Animal(object):
	def run(self):
		print("animal running...")
		return;

class Dog(Animal):
	pass

class Cat(Animal):
	def run(self):
		print("cat is running..")
		return;

dog = Dog()
#dog.run()

cat = Cat()
#cat.run()

#print("cat 是不是(isinstance) Animal:",isinstance(cat,Animal))
#print("dog 是不是(isinstance) Animal:",isinstance(dog,Animal))



# 静态语言 和 动态语言

# python属于动态语言，考虑下面的代码

# 定一个方法，接收animal类型
def runTwice(animal):
	animal.run()
	animal.run()
	return
# 用cat调用当然可以，因为cat继承了animal
runTwice(cat)
# 创建了一个新的类，book，book没有继承animal
class Book(object):
	def run(self):
		print("book running...")
		return	
book = Book()
# 用book调用，竟然也可以。 这就是python的动态语言
runTwice(book)
		
'''
对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：

这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，都被视为“file-like object“。

许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。
'''