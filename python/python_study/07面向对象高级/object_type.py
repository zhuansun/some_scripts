# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

from object_type_hello import Hello
h = Hello()
h.hello("jane")

print(type(Hello))
print(type(h))

'''
hello jane 
<class 'type'>
<class 'object_type_hello.Hello'>

参考输出结果，我们可以看到Hello类的type就是type，而实例h的type是object_type_hello.Hello

对比一下说明什么呢？
【实例】的type是【类】
所以，其实我们口中和Hello类，也不过是type的一个实例


怎么证明呢？ 因为我们可以直接用type创建出一个普通的类
'''

def sayfn(self,name='world'):
	print("say %s" % name)
# 创建people类
People = type("People", (object,), dict(say=sayfn))
p = People()
p.say("jane")

'''
事实证明，这样创建一个类，也是可以的。
语法是：
{1} = tyle({2},{3},{4})

{1} ： 类的名字
{2} ： 类的名字
{3} ： 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
{4} ： class的方法名称与函数绑定，这里我们把函数ssayfn绑定到方法名say上。



为什么可以这么做呢？ 原因是因为，python在遇到：
class xxx():
	xxxx
形式定义的类的时候，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

'''


