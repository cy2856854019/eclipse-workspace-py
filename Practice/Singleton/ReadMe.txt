
python3 的几种创建单例模式的方式

1.python的模块(在python中可理解为对应一个文件)就是一个很好的天然单例，模块在第一个导入时，会生成.pyc文件，当第二次导入时，就会直接加载.pyc文件，而不会再次执行模块代码
如cookie.py文件的变量cookies, 如果在别的文件中用from cookie import cookies导入，则cookies就成了一个单例

2.使用__new__()函数
__new__()和__init__的区别： 前者时类创建对象实例时调用，后者是在创建问对象实例后初始化时调用
class Singleton:
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, '_instance'):
			cls.instance = super().__new__(cls)
		return cls._instance

3.使用装饰器(装饰器，即将函数、类等作为参数传给装饰器函数)
from functools import wraps

def Singleton(cls):
	instances = {}
	@wraps(cls)
	def getinstance(*args, **kwargs):
		if cls not in instances:
			instances[cls] = cls(*args, **kwargs)
		return instances
	return getinstance
	
@Singleton
class Bar:
	pass

b0 = Bar()
b1 = Bar()
print(id(b0))
print(id(b1))

4.使用元类(元类可以控制类的创建过程)
class Singleton(type):
	'''
	元类继承于type
	'''
	_instance = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instance:
			cls._instance[cls] = super().__call__(*args, **kwargs)
		return cls._instance
class Bar(metaclass=Singleton)
	pass

b0 = Bar()
b1 = Bar()
print(id(b0))
print(id(b1))	
	
	
	
	


