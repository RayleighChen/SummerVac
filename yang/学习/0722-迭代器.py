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
>>> next(o��
     
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
>>> #������
>>> from collections import Iterable
>>> isinstance([], Iterable)
True
>>> isinstance((x for x in range(10)), Iterable)
True
>>> isinstance('abc', Iterable)
True
>>> isinstance({}, Iterable)
True
>>> #����������������������forѭ���������Ա�next()�������ϵ��ò�������һ��ֵ��ֱ������׳�StopIteration�����ʾ�޷�����������һ��ֵ��
>>> #���Ա�next()�������ò����Ϸ�����һ��ֵ�Ķ����Ϊ��������Iterator��
>>> #����ʹ��isinstance()�ж�һ�������Ƿ���Iterator����
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
>>> #����������Iterator���󣬵�list��dict��str��Ȼ��Iterable��ȴ����Iterator��
>>> #��list��dict��str��Iterable���Iterator����ʹ��iter()������
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True
>>> #list��dict��str���������Ͳ���Iterator��
>>> #������ΪPython��Iterator�����ʾ����һ����������Iterator������Ա�next()�������ò����Ϸ�����һ�����ݣ�ֱ��û������ʱ�׳�StopIteration���󡣿��԰����������������һ���������У�������ȴ������ǰ֪�����еĳ��ȣ�ֻ�ܲ���ͨ��next()����ʵ�ְ��������һ�����ݣ�����Iterator�ļ����Ƕ��Եģ�ֻ������Ҫ������һ������ʱ���Ż����
>>> #Iterator�������Ա�ʾһ�����޴��������������ȫ����Ȼ������ʹ��list����Զ�����ܴ洢ȫ����Ȼ����
