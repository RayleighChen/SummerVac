Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #�����ؼ��ֲ���
>>> def person(name,age,**kw):
	if 'city' in kw:
		#��city����
		pass
	if 'job' in kw:
		#��job����
		pass
	print('name:',name,'age:',age,'other:',kw)

	
>>> person('yhy',22,city='Beijing',address='haidian',zipcode=123456)
('name:', 'yhy', 'age:', 22, 'other:', {'city': 'Beijing', 'zipcode': 123456, 'address': 'haidian'})
>>> #�������Կ��Դ��벻�����ƵĹؼ��ֲ���,���Ҫ���ƹؼ��ֲ��������֣��Ϳ����������ؼ��ֲ��������磬ֻ����city��job��Ϊ�ؼ��ֲ��������ַ�ʽ����ĺ�������
>>> def person(name,age,*,city,job):
	
SyntaxError: invalid syntax
>>> def person(name,age,*,city,job):
	
SyntaxError: invalid syntax
>>> def person(name,age,*,city,job):
	
SyntaxError: invalid syntax
>>> def person(name, age, *, city, job):
	
SyntaxError: invalid syntax
>>> def person(name, age, *, city, job):
    print(name, age, city, job)
    
SyntaxError: invalid syntax
>>> def person(name, age, *args, city, job):
    print(name, age, args, city, job)
    
SyntaxError: invalid syntax
>>> def person1(name, age, *, city, job):
	
SyntaxError: invalid syntax
>>> #���ﲻ����
>>> def person(name, age, *, city='Beijing', job):
	
SyntaxError: invalid syntax
>>> #�������
>>> #���������˳������ǣ���ѡ������Ĭ�ϲ������ɱ�����������ؼ��ֲ����͹ؼ��ֲ���
>>> def f1(a,b,c=0,*args,**kw):
	print('a=',a,'b=',b,'c=',c,'args',args,'kw',kw)

	
>>> def f2(a,b,c=0,*,d,**kw):
	
SyntaxError: invalid syntax
>>> f1(1,2)
('a=', 1, 'b=', 2, 'c=', 0, 'args', (), 'kw', {})
>>> f1(1,2,c=3)
('a=', 1, 'b=', 2, 'c=', 3, 'args', (), 'kw', {})
>>> f1(1,2,3,'a','b')
('a=', 1, 'b=', 2, 'c=', 3, 'args', ('a', 'b'), 'kw', {})
>>> f1(1,2,3,'a','c',x=99)
('a=', 1, 'b=', 2, 'c=', 3, 'args', ('a', 'c'), 'kw', {'x': 99})
>>> #�ݹ麯��
>>> def fact(n):
	if n=1:
		
SyntaxError: invalid syntax
>>> def fact(n):
    if n==1:
	    return 1
	return n*fact(n-1)
  File "<pyshell#36>", line 5
    return n*fact(n-1)
                     ^
IndentationError: unindent does not match any outer indentation level
>>> def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

>>> def a(n):
    if n==1:
	return 1
    return n*a(n-1)

>>> def b(n):
	if n==1:
		return 1
	return n*b(n-1)

>>> #��������
>>> b(5)
120
>>> a(8)
40320
>>> #ʹ�õݹ麯����Ҫע���ֹջ������ڼ�����У�����������ͨ��ջ��stack���������ݽṹʵ�ֵģ�ÿ������һ���������ã�ջ�ͻ��һ��ջ֡��ÿ���������أ�ջ�ͻ��һ��ջ֡������ջ�Ĵ�С�������޵ģ����ԣ��ݹ���õĴ������࣬�ᵼ��ջ�������������fact(1000)
>>> fact(1000)

Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    fact(1000)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#38>", line 4, in fact
    return n * fact(n - 1)
RuntimeError: maximum recursion depth exceeded
>>> #����ݹ����ջ����ķ�����ͨ��β�ݹ��Ż�����ʵ��β�ݹ��ѭ����Ч����һ���ģ����ԣ���ѭ��������һ�������β�ݹ麯��Ҳ�ǿ��Ե�
>>> #β�ݹ���ָ���ں������ص�ʱ�򣬵������������ң�return��䲻�ܰ������ʽ�����������������߽������Ϳ��԰�β�ݹ����Ż���ʹ�ݹ鱾�����۵��ö��ٴΣ���ֻռ��һ��ջ֡���������ջ��������
>>> def fact(n):
	return fact_iter(n,1)

>>> def fact_iter(num,product):
	if num==1:
		return product
	return fact_iter(num-1,num*product)

>>> fact(5)
120
>>> fact(100)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000L
>>> fact(1000)

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    fact(1000)
  File "<pyshell#59>", line 2, in fact
    return fact_iter(n,1)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
  File "<pyshell#64>", line 4, in fact_iter
    return fact_iter(num-1,num*product)
