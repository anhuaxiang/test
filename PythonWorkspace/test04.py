# names=["gong","si","ya"]
# for name in names:
#	print(name)

# sum = 0
# for x in range(101):
# 	sum = sum +x
# print(sum)

# sum = 0
# n =99
# while n>0:
# 	sum=sum+n
# 	n=n-2
# print(sum)

# l=['xiaoyan','xiaoya','aiai']
# for lx in l:
# 	print("hello",lx)

# def my_abs(x):
# 	if not isinstance(x,(int,float)):
# 		raise TypeError('cuole')
# 	if(x>0):
# 		return x;
# 	else:
# 		return -x;
# print(my_abs(-10.3))

# def my_def():
# 	return 1,2
# x,y=my_def()
# print(x,y)

# def my_def():
# 	return 1,2
# x=my_def()
# print(x)

# import math
# def quadratic(a,b,c):
# 	if not isinstance(a,(int,float)):
# 		raise TypeError('参数a类型错误')
# 		return None,None
# 	if not isinstance(b,(int,float)):
# 		raise TypeError('参数b类型错误')
# 		return None,None
# 	if not isinstance(c,(int,float)):
# 		raise TypeError('参数c类型错误')
# 		return None,None
# 	if a==0 and b==0:
# 		print("a,b不能同时为0")
# 		return None,None
# 	else:
# 		if a==0:
# 			return -c/b,-c/b
# 		else:
# 			x=(b*b-4*a*c)
# 			if x>=0:
# 				y=math.sqrt(b*b-4*a*c)
# 				return (-b+y)/2/a,(-b-y)/2/a
# 			else:
# 				print("表达式没有实根")
# 				return None,None
# print(quadratic(1,-3,2))
# print(quadratic(0,3,-1))
# print(quadratic(0,0,1))
# print(quadratic(1,1,1))
# print(quadratic('a',2,3))
# print(quadratic('a','b','c'))

# def power(x,n=1):
# 	s=1
# 	while n>0:
# 		s=s*x
# 		n=n-1
# 	return s
# print(power(4,3))
# print(power(2))

# def enroll(name,grad,age=20,city='甘肃'):
# 	print('name',name)
# 	print('grad',grad)
# 	print('age',age)
# 	print('city',city)
# enroll('小闫','大三')
# enroll('小雅','大三',city='湖南

# def calc(numbers):
# 	sum=0
# 	for x in numbers:
# 		sum=sum+x*x
# 	return sum
# print(calc([1,2]))
# print(calc((1,2,3,4,5)))

# def calc(* numbers):
# 	sum=0
# 	for x in numbers:
# 		sum=sum+x*x
# 	return sum
# print(calc(1,2))
# print(calc(1,2,3,4,5))
# print(calc())
# nums=[1,2,3]
# print(calc(*nums))  

# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
# person('Michael', 30)
# person('Bob', 35, city='Beijing')
# person('Adam', 45, gender='M', job='Engineer')
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, city=extra['city'], job=extra['job'])
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, **extra)
# print(person('Jack', 24, **extra))

# from tkinter import *
# import tkinter.messagebox as messagebox

# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()

#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', 'Hello, %s' % name)

# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()

# def fact(n):
# 	x=1
# 	s=1
# 	while x<=n:
# 		s=s*x
# 		x=x+1
# 	return s
# print(fact(5))

# def fact1(n):
# 	if n==1:
# 		return 1
# 	else:
# 		return n*fact1(n-1)
# print(fact1(100))

# L=[]
# n=99
# while n>=1:
# 	L.append(n)
# 	n=n-2
# print(L)
# print(L[10:20])
# print(L[-10:-1])
# print(L[::5])

# for x,y in [(1,2),(3,4),(5,6)]:
# 	print(x,y)

# print(list(range(1,11)))

# L=[]
# for x in range(1,11):
# 	L.append(x*x)
# print(L)

# print([x*x for x in range(1,11) if x%2==0])

# print([m+n for m in 'xy' for n in 'ab'])

# import os
# print([d for d in os.listdir('.')])

# L = ['Hello', 'World', 'IBM', 'Apple']
# print([s.lower() for s in L])

# g=(x*x for x in range(1,11))
# print(next(g))
# print(next(g))

# g=(x*x for x in range(1,11))
# for y in g:
# 	print(y)

# def fib(max):
# 	n=1;m=1
# 	print(n)
# 	while m<=max:
# 		print(m)
# 		x=n
# 		n=m;m=m+x
# 	return 'done'
# print(fib(100))
# print(fib(1))

# def fib(max):
# 	n=1;m=1
# 	yield n
# 	while m<=max:
# 		yield m
# 		x=n
# 		n=m;m=m+x
# 	return 'done'
# a=(fib(100))
# for x in a:
# 	print(x)

# def myabs(a,b,c):
# 	return c(a)+c(b)
# print(myabs(-1,-3,abs))

# def f(x):
# 	return x*x
# r=map(f,[1,2,3,4,5,6,7,8,9])
# print(list(r))

# from functools import reduce
# def myadd(x,y):
# 	return x+y
# print(reduce(myadd,[1,2,3,4,5,6,7,8,9,10]))

# from functools import reduce
# def fun(x,y):
# 	return 10*x+y
# print(reduce(fun,[1,2,3,4,5,6,7,8,9]))

# def is_odd(n):
# 	return n%2==0
# l=filter(is_odd,[1,2,3,4,5,6,7,8,9])
# print(list(l))

# def initit():
# 	n=1
# 	while True:
# 		n=n+2
# 		yield n
# def not_divi(n):
# 	return lambda x:x%n>0
# def primes():
# 	yield 2
# 	it=initit()
# 	while(True):
# 		n=next(it)
# 		yield n
# 		it=filter(not_divi(n),it)
# for n in primes():
# 	if n<1000:
# 		print(n)

# print(sorted([26,21,-1,-23]))
# print(sorted([26,21,-1,-23],key=abs))
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

# def calc_sum(*args):
#     ax = 0
#     for n in args:
#         ax = ax + n
#     return ax
# print(calc_sum(1,2,3))

# class Student(object):
# 	def __init__(self,name,score):
# 		self.name=name
# 		self.score=score
# 	def intro(self):
# 		print(self.name,self.score)
# 	def get_gard(self):
# 		if self.score>90:
# 			return 'A'
# 		else:
# 			return 'B'
# student = Student('xiaoyan',85)
# student.intro()
# print(student.get_gard())

# class Student(object):
# 	def __init__(self,name,score):
# 		self.set_name(name)
# 		self.set_score(score)

# 	def set_name(self,name):
# 		self._name=name
# 	def set_score(self,score):
# 		if 0<=score<=100:
# 			self._score=score
# 		else:
# 			raise ValueError('参数成绩无效')
# 	def get_name(self):
# 		return self._name
# 	def get_score(self):
# 		return self._score

# 	def intro(self):
# 		print(self._name,self._score)
# 	def get_gard(self):
# 		if self._score>90:
# 			return 'A'
# 		else:
# 			return 'B'

# student = Student('xiaoyan',85)
# student.intro()
# print(student.get_gard())
# print(student.get_name())
# print(student.get_score())
# student1 = Student('xiaoya',101)













