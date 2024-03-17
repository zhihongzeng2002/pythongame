class Animal(object):
    def __init__(self, age):
        self.age = age

obj_animal = Animal(1)
obj_animal2 = Animal(15)
obj_animal3 = Animal(86)
obj_animal4 = Animal(100)
print(obj_animal)
print(obj_animal.age)
print(obj_animal2.age)
print(obj_animal3.age)
print(obj_animal4.age)