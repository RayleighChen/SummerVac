Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #高阶函数
>>> x=abs(-10)
>>> x
10
>>> f=abs
>>> f
<built-in function abs>
>>> f(-9)
9
>>> #传入函数
>>> #既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
>>> def add(x,y,f):
	return f(x)+f(y)

>>> add(-4,-9,abs)
13
>>> #map和reduce
>>> def f(x):
	return x*x

>>> r=map(f,[1,2,3,4,5,6,7,8,9])
>>> list(r)
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> list(map(str,[1,2,3,4,5,6]))
['1', '2', '3', '4', '5', '6']
>>> #再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是
>>> reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4）
				
SyntaxError: invalid syntax
>>> #？
>>> #比方说对一个序列求和，就可以用reduce实现：
>>> from functools import reduce
>>> def add(x,y):
	return x+y

>>> reduce(add,[1,3,5,7,9,11])
36
>>> #求和运算可以直接用Python内建函数sum()，没必要动用reduce.但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
>>> from functools import reduce
>>> def fn(x,y):
	return x*10+y

>>> reduce(fn,[1,3,5,6,4])
13564
>>> def char2num(s):
	 return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

	
>>> reduce(fn,map(char2num,'123467'))
123467
>>> #整理成一个str2int的函数就是：
>>> def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return {'0':0,'1':1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn,map(char2num,s))

>>> str2int('9830')
9830
>>> #还可以用lambda函数进一步简化成：
>>> def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
	
SyntaxError: invalid syntax
>>> def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

>>> def str2int(s):
	return reduce(lambda x,y:x*10+y,map(char2num,s))

>>> str2int('32331434657680')
32331434657680L
>>> 
