Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #����
>>> abs(100)
100
>>> abs(1,2)

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    abs(1,2)
TypeError: abs() takes exactly one argument (2 given)
>>> #��Ϊabs�����Դ���һ���������Ҳ���������Ҳ������
>>> abs('a')

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    abs('a')
TypeError: bad operand type for abs(): 'str'
>>> max(1,2,7,44)
44
>>> min(1,3,5)
1
>>> #��������ת��
>>> int('123')
123
>>> a=float('12.33')
>>> b=str(a)
>>> b
'12.33'
>>> a
12.33
>>> bool(0)
False
>>> bool(1)
True
>>> bool('')
False
>>> a=abs
>>> a(-1)
1
>>> b=bool
>>> b(1)
True
>>> #�����������
>>> hex(100)
'0x64'
>>> #��ҵ
>>> n1=hex(255)
>>> n2=hex(1000)
>>> print(n1,n2)
('0xff', '0x3e8')
>>> #���庯��
>>> def my_abs(x):
	if x>=0:
		return x
	else x<0:
		
SyntaxError: invalid syntax
>>>  def my_abs(x):
	if x>=0:
		return x
	else:
		
  File "<pyshell#31>", line 2
    def my_abs(x):
    ^
IndentationError: unexpected indent
>>> def my_abs(x):
	if x>=0:
		return x
	else:
		
  File "<pyshell#31>", line 2
    def my_abs(x):
	    
  File "<pyshell#32>", line 7
    File "<pyshell#31>", line 2
                              ^
IndentationError: unindent does not match any outer indentation level
>>> def abs1(x):
	if x>=0:
		return x
	else:
		return -x

	
>>> abs1(-9)
9
>>> #����û��return���᷵��none
>>> def a();
SyntaxError: invalid syntax
>>> def a();
SyntaxError: invalid syntax
>>> def a1();
SyntaxError: invalid syntax
>>> def a():
	pass

>>> #pass��ռλ��
>>> age=20
>>> if age>18:
	pass
else:
	print('n')

	
>>> #��������
>>> abs1(1,2)

Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    abs1(1,2)
TypeError: abs1() takes exactly 1 argument (2 given)
>>> abs1('a')
'a'
>>> abs1('A')
'A'
>>> #Ϊʲôû�б���
>>> abs('A')

Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    abs('A')
TypeError: bad operand type for abs(): 'str'
>>> def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else:
		return -x

	
>>> my_abs('A')

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    my_abs('A')
  File "<pyshell#67>", line 3, in my_abs
    raise TypeError('bad operand type')
TypeError: bad operand type
>>> my_abs(1.2)
1.2
>>> import math
>>> def move(x,y,step,angle=0);
SyntaxError: invalid syntax
>>> def move(x,y,step,angle):
	nx=x+step*math.cos(angle)
	ny=y+step*math.sin(angle)
	return nx,ny

>>> x,y=move(1,1,2,math.pi/4)
>>> print(x,y)
(2.414213562373095, 2.414213562373095)
>>> #����ʵ��ֻ��һ�ּ���Python�������ص���Ȼ�ǵ�һֵ
>>> s=move(1,1,2,math.pi/6)
>>> print(s)
(2.7320508075688776, 2.0)
>>> #����ֵ��һ��tuple
>>> 
