Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #tuple
>>> classmates=('yhy','xhp','yyl')
>>> t=(1,2)
>>> t=()
>>> t
()
>>> #定义只有一个元素的tuple
>>> t=(1)
>>> t
1
>>> #显示只有元素的tuple需要逗号
>>> t=(1,)
>>> t
(1,)
>>> #tuple不可变
>>> #“可变”的tuple
>>> t=('a','b',['A','B'])
>>> t[2][0]='X'
>>> t[2][1]='Y'
>>> t
('a', 'b', ['X', 'Y'])
>>> #因为AB在一个list里面
>>> #条件判断
>>> age=20
>>> if age>10:
	print('your age is',age)
	print('adult')

	
('your age is', 20)
adult
>>> age=3
>>> if age> 18
SyntaxError: invalid syntax
>>> if age>18:
	print('your age is',age)
	print('adult')

	
>>> else:
	
SyntaxError: invalid syntax
>>> age=3
>>> if age>18:
	print('your age is',age)
	print('adult')
    else:
	    
  File "<pyshell#33>", line 5
    else:
        ^
IndentationError: unindent does not match any outer indentation level
>>> age=3
>>>  if age>18:
	print('your age is',age)
	print('adult')
	
  File "<pyshell#35>", line 2
    if age>18:
    ^
IndentationError: unexpected indent
>>> m=3
>>> if m>18:
	print('adult')

	
>>> else:
	
SyntaxError: invalid syntax
>>> n=6
>>> if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

    
('your age is', 3)
teenager
>>> s=1
>>> if s>18:
	print('Y')
else:
	print('N')

	
N
>>> k=2
>>> if k>18:
	print('adult')
elif:
	print('teenager')
	
SyntaxError: invalid syntax
>>> k=7
>>> if k>18:
	print('adult')
elif:
	print('teenager')
	
SyntaxError: invalid syntax
>>> l=3
>>> ifl>18:
	
SyntaxError: invalid syntax
>>> l=3
>>> if l>18:
	print('Y')
elif l>6:
	print('H')
else:
	print('S')

	
S
>>> print(1)
1
>>> if x:
	print('True')

	

Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    if x:
NameError: name 'x' is not defined
>>> x=3
>>> if x:
	print('True')

	
True
>>> 只要x是非零数值、非空字符串、非空list等就判断为True
SyntaxError: invalid syntax
>>> #只要x是非零数值、非空字符串、非空list等就判断为True
>>> 
