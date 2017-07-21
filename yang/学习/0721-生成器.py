Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #列表生成式
>>> list(range(1,11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> #生成1*1，2*2....
>>> [x*x for x in range(1,11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> [x*x for x in range(1,11) if x%2==0]
[4, 16, 36, 64, 100]
>>> #两层循环，全排列
>>> [m+n for m in 'ACB' for n in 'YXZ']
['AY', 'AX', 'AZ', 'CY', 'CX', 'CZ', 'BY', 'BX', 'BZ']
>>> d={'x':'A','y':'B','z':'C'}
>>> [k+'='+v for k,v in d.items()]
['y=B', 'x=A', 'z=C']
>>> #字符串小写
>>> L=['Hello','World','IBM','Apple']
>>> [s.lower() for s in L]
['hello', 'world', 'ibm', 'apple']
>>> #生成器
>>> L=[x*x for x in range(10)]
>>> l

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>  L = [x * x for x in range(10)]
 
  File "<pyshell#16>", line 2
    L = [x * x for x in range(10)]
    ^
IndentationError: unexpected indent
>>> [x * x for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> L=[x * x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g=(x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x02F81940>
>>> #创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator
>>> #如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：
>>> next(g)
0
>>> g=(x*x for x in range(10))
>>> for n in g:
...	print(n)
  File "<pyshell#27>", line 3
    ...	print(n)
    ^
IndentationError: expected an indented block
>>> for n in g:
...     print(n)
...
  File "<pyshell#28>", line 3
    ...     print(n)
    ^
IndentationError: expected an indented block
>>>  for n in g:
 ...     print(n)
 ...
 
  File "<pyshell#29>", line 2
    for n in g:
    ^
IndentationError: unexpected indent
>>> for n in g:
	print(n)

	
0
1
4
9
16
25
36
49
64
81
>>> #著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：1, 1, 2, 3, 5, 8, 13, 21, 34, ...
>>> def fib(max):
	n,a,b=0,0,1
	while n<max:
		print(b)
		a,b=b,b+a
		n=n+1
	return 'done'

>>> fib(6)
1
1
2
3
5
8
'done'
>>> fib(9)
1
1
2
3
5
8
13
21
34
'done'
>>> def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
SyntaxError: 'return' with argument inside generator (<pyshell#44>, line 8)
>>> def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,b+a
		n=n+1
	return 'done'
SyntaxError: 'return' with argument inside generator (<pyshell#45>, line 8)
>>> def fib(max):
	n,a,b=0,0,1
	while n<max:
		print(b)
		a,b=b,b+a
		n=n+1
	return 'done'

>>> def fib(max):
	n,a,b=0,0,1
	while n<max:
		yeild b
		a,b=b,b+a
		n=n+1
	return 'done'
SyntaxError: invalid syntax
>>> def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,b+a
		n=n+1
	return 'done
SyntaxError: EOL while scanning string literal
>>> def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
SyntaxError: 'return' with argument inside generator (<pyshell#50>, line 8)
>>> #?生成器部分疑问
