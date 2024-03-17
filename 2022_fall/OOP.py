class Animal():
    def __init__(self, age):
        self.age = age
    
    def speak(self):
        print("not defined")

    def __str__(self):
        return "Animal age: " + str(self.age)

class Cat(Animal):
    def __init__(self, age, color):
        super().__init__(age)
        self.color = color
    
    def __str__(self):
        return "Cat age: {}, cat color: {}".format(self.age, self.color)

class Lion(Cat):
    def __init__(self, age, color, size):
        super().__init__(age, color)
        self.size = size
    
    def speak(self):
        print("roar")

    def __lt__(self, other):
        return self.size < other.size

x = Animal(10)
x.speak()
print(x)

y = Animal(60)
print(y)

a = Cat(7, "Orange")
print(a)
a.speak()

b = Lion(15, "Yellow", 10)
b.speak()
print(b)

c = Lion(10, "Yellow", 13)

z = c > b
print(z)