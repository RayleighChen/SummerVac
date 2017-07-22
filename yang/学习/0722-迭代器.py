Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def fib(max):
	n,a,b=0,0,1
	while n < max:
		yield b
		a,b=b,a+b
		n=n+1
	return 'done'
SyntaxError: 'return' with argument inside generator (<pyshell#6>, line 8)
>>> def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done
SyntaxError: EOL while scanning string literal
>>> def fibonacci():  
    a=b=1  
    yield a  
    yield b  
    while True:  
        a,b = b,a+b  
        yield b

        
>>> fibonacci()
<generator object fibonacci at 0x02DB7788>
>>> def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

        
>>> fib(6)
<generator object fib at 0x02DB7170>
>>> f=fib(3)
>>> next(f)
1
>>> next(f)
1
>>> next(f)
2
>>> def odd():
	print('step1')
	yield 1
	print('step2')
	yield(3)
	print('step3')
	yield(5)

	
>>> o=odd()
>>> next(o)
step1
1
>>> next(o）
     
SyntaxError: invalid syntax
>>> next(o)
step2
3
>>> next(o)
step3
5
>>> for n in fib(6):
	print(n)

	
1
1
2
3
5
8
>>> #迭代器
>>> from collections import Iterable
>>> isinstance([], Iterable)
True
>>> isinstance((x for x in range(10)), Iterable)
True
>>> isinstance('abc', Iterable)
True
>>> isinstance({}, Iterable)
True
>>> #而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了
>>> #可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
>>> #可以使用isinstance()判断一个对象是否是Iterator对象：
>>> isinstance((x for x in range(10)), Iterator)

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    isinstance((x for x in range(10)), Iterator)
NameError: name 'Iterator' is not defined
>>> from collections import Iterator
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False
>>> isinstance('abc', Iterator)
False
>>> #生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
>>> #把list、dict、str等Iterable变成Iterator可以使用iter()函数：
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True
>>> #list、dict、str等数据类型不是Iterator？
>>> #这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算
>>> #Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的
