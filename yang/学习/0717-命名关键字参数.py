Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def power(x):
	return x*x

>>> power(2)
4
>>> #定义函数
>>> def power(x,n):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s

>>> #定义x^n的函数
>>> power(3,5)
243
>>> power(3)

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    power(3)
TypeError: power() takes exactly 2 arguments (1 given)
>>> #这时候可以用默认参数
>>> def power(x,n=2):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s

>>> power(4)
16
>>> power(4,2)
16
>>> #默认参数必须放在必选参数后面
>>> #小学生注册函数
>>> def eroll(name,gender):
	print('name: ',name)
	print('gender: ',gender)

	
>>> eroll('yhy','F')
('name: ', 'yhy')
('gender: ', 'F')
>>> #传入其他属性，设置默认参数
>>> eroll(name,gender,age=6,city='Beijing'):
	print('name: ',name)
	print('gender: ',gender)
	
SyntaxError: invalid syntax
>>> eroll(name,gender,age=6,city='Beijing'):
	print('name: ',name)
	print('gender: ',gender)
	
SyntaxError: invalid syntax
>>> enroll(name,gender,age=6,city='Beijing'):
	print('name: ',name)
	print('gender: ',gender)
	
SyntaxError: invalid syntax
>>> def enroll(name,gender,age=6,city='Beijing'):
	print('name: ',name)
	print('gender: ',gender)
	print('age: ',age)
	print('city: ',city)

	
>>> enroll('yhy','A')
('name: ', 'yhy')
('gender: ', 'A')
('age: ', 6)
('city: ', 'Beijing')
>>> #也可以传入与默认参数不同的值
>>> enroll('xhp','M',33,'Haiyang')
('name: ', 'xhp')
('gender: ', 'M')
('age: ', 33)
('city: ', 'Haiyang')
>>> def enroll1(name,gender,age=6,city='Beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)

	
>>> enroll1('yhy','A')
('name:', 'yhy')
('gender:', 'A')
('age:', 6)
('city:', 'Beijing')
>>> print(5,6)
(5, 6)
>>> #默认参数最大的坑
>>> def add_end(L=[]):
	L.append('END')
	return L

>>> add_end([1,2,3])
[1, 2, 3, 'END']
>>> add_end(['x','y','z'])
['x', 'y', 'z', 'END']
>>> add_end()
['END']
>>> add_end()
['END', 'END']
>>> add_end()
['END', 'END', 'END']
>>> #Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
>>> #所以，定义默认参数要牢记一点：默认参数必须指向不变对象
>>> #修改
>>> def add_end(L=None):
	if L is None:
		L=[]
	L.append('END')
	return L

>>> add_end()
['END']
>>> add_end()
['END']
>>> add_end([1,2,3])
[1, 2, 3, 'END']
>>> #可变参数
>>> #计算a^2+b^2+c^2+....
>>> def calc(numbers):
	sum=0
	for n in numbers:
		sum=sum+n*n
	return sum

>>> calc([1,3,4])
26
>>> #利用可变参数
>>> def calc(*number):
	sum=0
	for n in number:
		sum=n*n+sum
	return sum

>>> calc(1,2,3,4,5)
55
>>> #定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
>>> calc()
0
>>> #如果已经有一个list或者tuple，要调用一个可变参数怎么办？
>>> nums=[1,2,3]
>>> calc(nums[0],num[1],num[2])

Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    calc(nums[0],num[1],num[2])
NameError: name 'num' is not defined
>>> calc(nums[0],nums[1],nums[2])
14
>>> calc(*nums)
14
>>> #关键字参数
>>> def person(name,age,**kw)
SyntaxError: invalid syntax
>>> def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

	
>>> person('yhy',20)
('name:', 'yhy', 'age:', 20, 'other:', {})
>>> person('yhy',20,city='Beijng')
('name:', 'yhy', 'age:', 20, 'other:', {'city': 'Beijng'})
>>> person('yhy',20,gender='A',city='haiyang')
('name:', 'yhy', 'age:', 20, 'other:', {'gender': 'A', 'city': 'haiyang'})
>>> #和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
>>> extra= {'city': 'Beijing', 'job': 'Engineer'}
>>> person('yhy',22,**extra)
('name:', 'yhy', 'age:', 22, 'other:', {'city': 'Beijing', 'job': 'Engineer'})
>>> 
