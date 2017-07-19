Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #切片
>>> L=['yhy','xhp','yyl','yrl','cpc']
>>> L
['yhy', 'xhp', 'yyl', 'yrl', 'cpc']
>>> #提取前三个元素
>>> [L[0],L[1],L[2]]
['yhy', 'xhp', 'yyl']
>>> #循环方法
>>> r=[]
>>> n=3
>>> for i in range(n):
...     r.append(L[i])
  File "<pyshell#9>", line 3
    ...     r.append(L[i])
    ^
IndentationError: expected an indented block
>>> for i in range(n):
	...  r.append(L[i])
	
SyntaxError: invalid syntax
>>> for i in range(n):
...     r.append(L[i])
...
  File "<pyshell#12>", line 3
    ...     r.append(L[i])
    ^
IndentationError: expected an indented block
>>> for i in range(n):
...     r.append(L[i])
...
  File "<pyshell#13>", line 3
    ...     r.append(L[i])
    ^
IndentationError: expected an indented block
>>> for i in range(n):
...	r.append(L[i])
  File "<pyshell#15>", line 3
    ...	r.append(L[i])
    ^
IndentationError: expected an indented block
>>> #切片
>>> L[0:3]
['yhy', 'xhp', 'yyl']
>>> L[1:3]
['xhp', 'yyl']
>>> L[3:4]
['yrl']
>>>  S=['yhy','xhp','yyl','yrl','cpc']
 
  File "<pyshell#20>", line 2
    S=['yhy','xhp','yyl','yrl','cpc']
    ^
IndentationError: unexpected indent
>>> S=['yhy','xhp','yyl','yrl','cpc']
>>> S[-1:]
['cpc']
>>> S[-5]
'yhy'
>>> S[-2:-5]
[]
>>> S[-2:]
['yrl', 'cpc']
>>> S[-5:-2]
['yhy', 'xhp', 'yyl']
>>> M=list(range(100))
>>> M
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> M[:10]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> M[-10:]
[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> #第10-20个数字
>>> M[9:20]
[9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> #前10个数字，每两个取一个
>>> L[0:10:2]
['yhy', 'yyl', 'cpc']
>>> M[0:10:2]
[0, 2, 4, 6, 8]
>>> #每5个数字取一个
>>> L[::5]
['yhy']
>>> M[::5]
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
>>> L[:]
['yhy', 'xhp', 'yyl', 'yrl', 'cpc']
>>> M[:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> #tuple和字符串也可以此种操作
>>> 'ABCDGCXSDDDSFS'[:3]
'ABC'
>>> 'SDEGGJUYIKH'[:4]
'SDEG'
>>> #迭代
>>> #Python的for循环抽象程度要高于Java的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
>>> #list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
>>> d={'a':1,'b';2,'c':3}
SyntaxError: invalid syntax
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for key in d:
...	print(key)
  File "<pyshell#50>", line 3
    ...	print(key)
    ^
IndentationError: expected an indented block
>>>  for key in d:
...     print(key)
...
  File "<pyshell#51>", line 2
    for key in d:
    ^
IndentationError: unexpected indent
>>>  for key in d:
	...     print(key)
	...
	
  File "<pyshell#52>", line 2
    for key in d:
    ^
IndentationError: unexpected indent
>>> for key in d:
	...	print(key)
	
SyntaxError: invalid syntax
>>>  from collections import Iterable
 
  File "<pyshell#55>", line 2
    from collections import Iterable
    ^
IndentationError: unexpected indent
>>> from collections import Iterable
>>> #判断一个对象是否迭代
>>> isinstance('abc',Iterable) #str是否迭代
True
>>> isinstance([1,2,3],Iterable) #list是否迭代
True
>>> isinstance(123,Iterable) #整数是否迭代
False
>>>  for i, value in enumerate(['A', 'B', 'C']):
...     print(i, value)
...
  File "<pyshell#61>", line 2
    for i, value in enumerate(['A', 'B', 'C']):
    ^
IndentationError: unexpected indent
>>> #...	...部分总是报错
>>> 
