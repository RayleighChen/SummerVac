Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def power(x):
	return x*x

>>> power(2)
4
>>> #���庯��
>>> def power(x,n):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s

>>> #����x^n�ĺ���
>>> power(3,5)
243
>>> power(3)

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    power(3)
TypeError: power() takes exactly 2 arguments (1 given)
>>> #��ʱ�������Ĭ�ϲ���
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
>>> #Ĭ�ϲ���������ڱ�ѡ��������
>>> #Сѧ��ע�ắ��
>>> def eroll(name,gender):
	print('name: ',name)
	print('gender: ',gender)

	
>>> eroll('yhy','F')
('name: ', 'yhy')
('gender: ', 'F')
>>> #�����������ԣ�����Ĭ�ϲ���
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
>>> #Ҳ���Դ�����Ĭ�ϲ�����ͬ��ֵ
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
>>> #Ĭ�ϲ������Ŀ�
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
>>> #Python�����ڶ����ʱ��Ĭ�ϲ���L��ֵ�ͱ���������ˣ���[]����ΪĬ�ϲ���LҲ��һ����������ָ�����[]��ÿ�ε��øú���������ı���L�����ݣ����´ε���ʱ��Ĭ�ϲ��������ݾͱ��ˣ������Ǻ�������ʱ��[]�ˡ�
>>> #���ԣ�����Ĭ�ϲ���Ҫ�μ�һ�㣺Ĭ�ϲ�������ָ�򲻱����
>>> #�޸�
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
>>> #�ɱ����
>>> #����a^2+b^2+c^2+....
>>> def calc(numbers):
	sum=0
	for n in numbers:
		sum=sum+n*n
	return sum

>>> calc([1,3,4])
26
>>> #���ÿɱ����
>>> def calc(*number):
	sum=0
	for n in number:
		sum=n*n+sum
	return sum

>>> calc(1,2,3,4,5)
55
>>> #����ɱ�����Ͷ���һ��list��tuple������ȣ������ڲ���ǰ�����һ��*�š��ں����ڲ�������numbers���յ�����һ��tuple����ˣ�����������ȫ���䡣���ǣ����øú���ʱ�����Դ������������������0������
>>> calc()
0
>>> #����Ѿ���һ��list����tuple��Ҫ����һ���ɱ������ô�죿
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
>>> #�ؼ��ֲ���
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
>>> #�Ϳɱ�������ƣ�Ҳ��������װ��һ��dict��Ȼ�󣬰Ѹ�dictת��Ϊ�ؼ��ֲ�������ȥ
>>> extra= {'city': 'Beijing', 'job': 'Engineer'}
>>> person('yhy',22,**extra)
('name:', 'yhy', 'age:', 22, 'other:', {'city': 'Beijing', 'job': 'Engineer'})
>>> 
