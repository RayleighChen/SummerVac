Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #����input
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
	print('00ǰ')
else:
	print('00��'��
	      
SyntaxError: invalid syntax
>>> if brith<2000:
	print('00ǰ')

	
00ǰ
>>> if brith<2000:
	print('00ǰ')
else:
	print('00��')

	
00ǰ
>>> #��ϰ
>>> h=1.75
>>> w=80.5
>>> b1=80.5/1.75
>>> b=b1/h
>>> print(b)
26.2857142857
>>> if b<18.5:
	print('����')
elif b>18.5&&b<25:
	
SyntaxError: invalid syntax
>>> if b<18.5:
	print('����')
elif b>18.5 and b<25:
	print('����')
else:
	print('����')

	
����
>>> #ʹ��dict��set
>>> d={'yhy':99,'xhp':98,'yyl':90}
>>> d{'yhy'}
SyntaxError: invalid syntax
>>> d['yhy']
99
>>> #list����Ҫ����list���洢
>>> d['yhy1']=96
>>> d
{'xhp': 98, 'yyl': 90, 'yhy': 99, 'yhy1': 96}
>>> d['yhy']=99
>>> d
{'xhp': 98, 'yyl': 90, 'yhy': 99, 'yhy1': 96}
>>> #һ��key������Ӧһ��value����η���value���ǰ���ֵ���
>>> ��yhy2' in d
SyntaxError: invalid syntax
>>> 'yhy2' in d
False
>>> #key�����ڻᱨ���ж�key������񣬿��������Ϸ���
>>> d.get('yhy2')
>>> d.get('yhy',0)
99
>>> d.get('yhy2',0)
0
>>> #���key�����ڣ����Է���none��Ҳ�����Լ�����
>>> d.pop('yhy1')
96
>>> d
{'xhp': 98, 'yyl': 90, 'yhy': 99}
>>> #ɾ��key
>>> #dict����������Ҫ���ٲ��ҵĺܶ�ط�����Python�����м����޴����ڣ���ȷʹ��dict�ǳ���Ҫ����Ҫ�μǵĵ�һ������dict��key�����ǲ��ɱ����

������Ϊdict����key������value�Ĵ洢λ�ã����ÿ�μ�����ͬ��key�ó��Ľ����ͬ����dict�ڲ�����ȫ�����ˡ����ͨ��key����λ�õ��㷨��Ϊ��ϣ�㷨��Hash����

Ҫ��֤hash����ȷ�ԣ���Ϊkey�Ķ���Ͳ��ܱ䡣��Python�У��ַ����������ȶ��ǲ��ɱ�ģ���ˣ����Է��ĵ���Ϊkey����list�ǿɱ�ģ��Ͳ�����Ϊkey
SyntaxError: invalid syntax
>>> #set��dict���ƣ�Ҳ��key�ļ��ϣ�����key�����ظ�������set��û���ظ���key
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
>>> #set�����������Ȳ���
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
>>> #str�ǲ��ɱ����list�ǿɱ����
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
