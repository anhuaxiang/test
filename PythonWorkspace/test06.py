# class Student(object):
#     pass
# s=Student()
# s.name='xiaoya'
# print(s.name)
#
# def set_age(self,age):
#     self.age=age
#
# from types import MethodType
# s.set_age=MethodType(set_age,s)
# s.set_age(20)
# print(s.age)
# print(dir(s))
#
# Student.set_age=set_age
# s1 = Student()
# s1.set_age(21)
# print(s1.age)

# class Student(object):
#     _slots_=('name','score') # 仅存在啷个属相，外加属相会出错

# class Student(object):
#
#     def set_score(self,score):
#         if not isinstance(score,(int,float)):
#             raise ValueError('参数类型错误')
#         if not 0<=score<=100:
#             raise ValueError('分数不对')
#         self.score=score
#     def get_score(self):
#         return self.score
# s=Student()
# s.set_score(101)
# print(s.get_score())

# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, score):
#         if not isinstance(score, (int, float)):
#             raise ValueError('参数类型错误')
#         if not 0 <= score <= 100:
#             raise ValueError('分数不对')
#         self._score = score
#
# s=Student()
# s.score=100
# print(s.score)

# class Student(object):
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return self.name
#     def __repr__(self):
#         return  self.name
# s=Student('龚思雅')
# print(s)
# print(Student('闫茹晶'))
#
# class Fib(object):
#     def __init__(self):
#         self.a,self.b=0,1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a,self.b=self.b,self.a+self.b
#         if self.a>10000:
#             raise StopIteration()
#         return self.a
#
# fib=Fib()
# for n in fib:
#     print(n)


# a=0;b=1
# while(a<10000):
#     c=a;a=b;b=c+b
#     print(a)

# a,b=0,1
# while(a<1000):
#     a,b=b,b+a
#     print(a)

class Fib(object):

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 0, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f = Fib()
print(f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8], f[9], f[10])
print(f[2:10])
