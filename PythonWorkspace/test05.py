import types


class Animal(object):

    def run(self):
        print('animal is runing...')


class Dog(Animal):

    def run(self):
        print('dog is running')


class Cat(Animal):

    def run(self):
        print('cat is running')

    def eat(self):
        print('eating fish')

animal = Animal()
animal.run()
dog = Dog()
dog.run()
cat = Cat()
cat.run()
cat.eat()
print(isinstance(dog, Animal))


def run_twice(animal):
    animal.run()
    animal.run()
run_twice(animal)
run_twice(dog)
run_twice(cat)


class Timer(object):

    def run(self):
        print('Time is running')


run_twice(Timer())

print(type(dog), '************')
print(type(abs))

print(type(123) == type(456))
print(type(animal) == type(Animal()))
print(type(animal) == type(dog))

print(type(run_twice) == types.FunctionType)
print(type(abs) == types.FunctionType)

print(isinstance(dog, Dog))
print(dir(dog))

print(hasattr(dog, 'x'))
print(getattr(dog, 'x', '类中没有这个属性'))
print(hasattr(dog, 'run'))
print(getattr(dog, 'run'))


class Student(object):
    name = 'btudent'
s = Student()
print(s.name)
s.name = 'nihao'
print(s.name)
print(Student.name)
