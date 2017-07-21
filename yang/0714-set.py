Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #再议input
>>> s=input('brith:')
brith:1994
>>> brith=int(b)

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    brith=int(b)
NameError: name 'b' is not defined
>>> brith=int(s)
>>> brith
1994
>>> if brith<2000:
	print('00前')
else:
	print('00后'）
	      
SyntaxError: invalid syntax
>>> if brith<2000:
	print('00前')

	
00前
>>> if brith<2000:
	print('00前')
else:
	print('00后')

	
00前
>>> #练习
>>> h=1.75
>>> w=80.5
>>> b1=80.5/1.75
>>> b=b1/h
>>> print(b)
26.2857142857
>>> if b<18.5:
	print('过轻')
elif b>18.5&&b<25:
	
SyntaxError: invalid syntax
>>> if b<18.5:
	print('过轻')
elif b>18.5 and b<25:
	print('正常')
else:
	print('过重')

	
过重
>>> #使用dict和set
>>> d={'yhy':99,'xhp':98,'yyl':90}
>>> d{'yhy'}
SyntaxError: invalid syntax
>>> d['yhy']
99
>>> #list则需要两个list来存储
>>> d['yhy1']=96
>>> d
{'xhp': 98, 'yyl': 90, 'yhy': 99, 'yhy1': 96}
>>> d['yhy']=99
>>> d
{'xhp': 98, 'yyl': 90, 'yhy': 99, 'yhy1': 96}
>>> #一个key仅仅对应一个value，多次放入value会把前面的值冲掉
>>> ‘yhy2' in d
SyntaxError: invalid syntax
>>> 'yhy2' in d
False
>>> #key不存在会报错，判断key存在与否，可以用以上方法
>>> d.get('yhy2')
>>> d.get('yhy',0)
99
>>> d.get('yhy2',0)
0
>>> #如果key不存在，可以返回none，也可以自己定义
>>> d.pop('yhy1')
96
>>> d
{'xhp': 98, 'yyl': 90, 'yhy': 99}
>>> #删除key
>>> #dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key
SyntaxError: invalid syntax
>>> #set与dict类似，也是key的集合，由于key不能重复，所以set中没有重复的key
>>> s=set([1,2,3,4])
>>> s
set([1, 2, 3, 4])
>>> s=set([1,2,2,3,4,4,5])
>>> s
set([1, 2, 3, 4, 5])
>>> s.add(3)
>>> s
set([1, 2, 3, 4, 5])
>>> s.add(10)
>>> s
set([1, 2, 3, 4, 5, 10])
>>> s.remove(10)
>>> s
set([1, 2, 3, 4, 5])
>>> #set可以做交并等操作
>>> s1=([1,2,4])
>>> s2=([1,2,5,7])
>>> s1&2

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    s1&2
TypeError: unsupported operand type(s) for &: 'list' and 'int'
>>> s1&s2

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    s1&s2
TypeError: unsupported operand type(s) for &: 'list' and 'list'
>>> s1 &s2

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    s1 &s2
TypeError: unsupported operand type(s) for &: 'list' and 'list'
>>> s3=([1,2,3])
>>> s1 &s3

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s1 &s3
TypeError: unsupported operand type(s) for &: 'list' and 'list'
>>> m1=set([1,2,3])
>>> m2=set([1,2,4,7])
>>> m1&m2
set([1, 2])
>>> m1 | m2
set([1, 2, 3, 4, 7])
>>> #str是不可变对象，list是可变对象
>>> a='abc'
>>> a.sort()

Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a.sort()
AttributeError: 'str' object has no attribute 'sort'
>>> a.repalce('a','A')

Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.repalce('a','A')
AttributeError: 'str' object has no attribute 'repalce'
>>> a.replace('a','A')
'Abc'
>>> a
'abc'
>>> a=['a','c','b']
>>> a.sort()
>>> a
['a', 'b', 'c']
>>> b=a.replace()

Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    b=a.replace()
AttributeError: 'list' object has no attribute 'replace'
>>> b=a.replace('a','A')

Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    b=a.replace('a','A')
AttributeError: 'list' object has no attribute 'replace'
>>> b = a.replace('a', 'A')

Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    b = a.replace('a', 'A')
AttributeError: 'list' object has no attribute 'replace'
>>> a='abc'
>>> b = a.replace('a', 'A')
>>> b
'Abc'
>>> a
'abc'
>>> 
