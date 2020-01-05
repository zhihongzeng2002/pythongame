class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self, greeting):
        print(greeting + ' ' + self.name)

x = Person('John', 10)
x.hello('Hello')
print(x.age)
x.age = 20
print(x.age)

    
def hello(name, greeting):
    print(greeting + ' ' + name)

hello('John', 'Hello')

class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def print_grade(self):
        print(self.name + ' is at Grade ' + str(self.grade))

y = Student('Peter', 10, 4)
y.hello('Hello')
y.print_grade()

class Professor(Person):

    def __init__(self, name, age):
        super().__init__(name, age)

    def hello(self, greeting):
        print(greeting + ' Prof ' + self.name)

p = Professor('Gates', 10)
p.hello('Hello')

