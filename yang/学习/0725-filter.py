Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #filter
>>> #��������
>>> #��������
>>> #
>>> #��map()���ƣ�filter()Ҳ����һ��������һ�����С���map()��ͬ���ǣ�filter()�Ѵ���ĺ�������������ÿ��Ԫ�أ�Ȼ����ݷ���ֵ��True����False�����������Ƕ�����Ԫ�ء�
>>> def is_odd(n):
	return n%2==1

>>> list(filter(is_odd,[1,2,3,4,5,6,7,8]))
[1, 3, 5, 7]
>>> list([1,3,4])
[1, 3, 4]
>>> def not_empty(s):
	return s and s.strip()

>>> list(filter(not_empty,['A','B','C',None,' ']))
['A', 'B', 'C']
>>> #��һ�������еĿ��ַ���ɾ��
>>> #ɸѡ����
>>> def_odd_iter():
	
SyntaxError: invalid syntax
>>> def _odd_iter():
	n=1
	while True:
		n=n+2
		yield n

		
>>> #ע������һ����������������һ���������С�
>>> #Ȼ����һ��ɸѡ����:
>>> def _not_divisible(n):
	return lambda x:x%n>0

>>> #��󣬶���һ�������������Ϸ�����һ��������
>>> def primes();
SyntaxError: invalid syntax
>>> def primes():
	yield 2
	it=_odd_iter() #��ʼ����
	while True:
		n=next(it) #�������еĵ�һ����
		yield n
		it=filter(_not_divisible(n),it) #����������

		
>>> for n in primes():
	if n<1000:
		print(n)
	else:
		break

	
2
3

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    for n in primes():
  File "<pyshell#39>", line 7, in primes
    it=filter(_not_divisible(n),it) #����������
MemoryError






>>> for n in primes():
    if n < 1000:
        print(n)
    else:
        break

2
3

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    for n in primes():
  File "<pyshell#39>", line 7, in primes
    it=filter(_not_divisible(n),it) #����������
MemoryError
















































>>> for n in primes():
    if n < 1000:
        print(n)

2
3

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    for n in primes():
  File "<pyshell#39>", line 7, in primes
    it=filter(_not_divisible(n),it) #����������
MemoryError


>>> def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

        
>>> def _not_divisible(n):
    return lambda x: x % n > 0

>>> def primes():
    yield 2
    it = _odd_iter() # ��ʼ����
    while True:
        n = next(it) # �������еĵ�һ����
        yield n
        it = filter(_not_divisible(n), it) # ����������

        
>>> for n in primes():
    if n < 1000:
        print(n)
    else:
        break

2
3

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    for n in primes():
  File "<pyshell#54>", line 7, in primes
    it = filter(_not_divisible(n), it) # ����������
MemoryError

>>> 
