Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #filter
>>> #过滤序列
>>> #过滤序列
>>> #
>>> #和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
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
>>> #把一个序列中的空字符串删掉
>>> #筛选素数
>>> def_odd_iter():
	
SyntaxError: invalid syntax
>>> def _odd_iter():
	n=1
	while True:
		n=n+2
		yield n

		
>>> #注意这是一个生成器，并且是一个无限序列。
>>> #然后定义一个筛选函数:
>>> def _not_divisible(n):
	return lambda x:x%n>0

>>> #最后，定义一个生成器，不断返回下一个素数：
>>> def primes();
SyntaxError: invalid syntax
>>> def primes():
	yield 2
	it=_odd_iter() #初始序列
	while True:
		n=next(it) #返回序列的第一个数
		yield n
		it=filter(_not_divisible(n),it) #构造新序列

		
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
    it=filter(_not_divisible(n),it) #构造新序列
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
    it=filter(_not_divisible(n),it) #构造新序列
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
    it=filter(_not_divisible(n),it) #构造新序列
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
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

        
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
    it = filter(_not_divisible(n), it) # 构造新序列
MemoryError

>>> 
