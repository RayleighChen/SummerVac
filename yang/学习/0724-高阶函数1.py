Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #�߽׺���
>>> x=abs(-10)
>>> x
10
>>> f=abs
>>> f
<built-in function abs>
>>> f(-9)
9
>>> #���뺯��
>>> #��Ȼ��������ָ�����������Ĳ����ܽ��ձ�������ôһ�������Ϳ��Խ�����һ��������Ϊ���������ֺ����ͳ�֮Ϊ�߽׺���
>>> def add(x,y,f):
	return f(x)+f(y)

>>> add(-4,-9,abs)
13
>>> #map��reduce
>>> def f(x):
	return x*x

>>> r=map(f,[1,2,3,4,5,6,7,8,9])
>>> list(r)
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> list(map(str,[1,2,3,4,5,6]))
['1', '2', '3', '4', '5', '6']
>>> #�ٿ�reduce���÷���reduce��һ������������һ������[x1, x2, x3, ...]�ϣ�������������������������reduce�ѽ�����������е���һ��Ԫ�����ۻ����㣬��Ч������
>>> reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4��
				
SyntaxError: invalid syntax
>>> #��
>>> #�ȷ�˵��һ��������ͣ��Ϳ�����reduceʵ�֣�
>>> from functools import reduce
>>> def add(x,y):
	return x+y

>>> reduce(add,[1,3,5,7,9,11])
36
>>> #����������ֱ����Python�ڽ�����sum()��û��Ҫ����reduce.�������Ҫ������[1, 3, 5, 7, 9]�任������13579��reduce�Ϳ��������ó���
>>> from functools import reduce
>>> def fn(x,y):
	return x*10+y

>>> reduce(fn,[1,3,5,6,4])
13564
>>> def char2num(s):
	 return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

	
>>> reduce(fn,map(char2num,'123467'))
123467
>>> #�����һ��str2int�ĺ������ǣ�
>>> def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return {'0':0,'1':1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn,map(char2num,s))

>>> str2int('9830')
9830
>>> #��������lambda������һ���򻯳ɣ�
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
