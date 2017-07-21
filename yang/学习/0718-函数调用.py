Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #命名关键字参数
>>> def person(name,age,**kw):
	if 'city' in kw:
		#有city参数
		pass
	if 'job' in kw:
		#有job函数
		pass
	print('name:',name,'age:',age,'other:',kw)

	
>>> person('yhy',22,city='Beijing',address='haidian',zipcode=123456)
('name:', 'yhy', 'age:', 22, 'other:', {'city': 'Beijing', 'zipcode': 123456, 'address': 'haidian'})
>>> #调用者仍可以传入不受限制的关键字参数,如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下
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
>>> #这里不明白
>>> def person(name, age, *, city='Beijing', job):
	
SyntaxError: invalid syntax
>>> #参数组合
>>> #参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
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
>>> #递归函数
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

>>> #对齐问题
>>> b(5)
120
>>> a(8)
40320
>>> #使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)
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
>>> #解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的
>>> #尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况
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
