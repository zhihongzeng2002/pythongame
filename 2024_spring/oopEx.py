#make mouse object with attributes:
#name, color
#mouse has behavior:
#print "squeak", print its name

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cat(Animal):
    def speak(self):
        print("meow")
        print("my name is " + self.name)

def speak(name):
    print("meow")
    print("my name is " + name)

dogObj = Animal("dog", 3)
print("my dog's name is: " + dogObj.name)
print("my dog's age is: " + str(dogObj.age))


catObj1 = Cat("cat", 5)
print("my cat's name is: " + catObj1.name)
print("my cat's age is: " + str(catObj1.age))

catObj2 = Cat("alfred", 2)
print("my cat's name is: " + catObj2.name)
print("my cat's age is: " + str(catObj2.age))

catObj3 = Cat("buler", 69)

catObj4 = Cat("boca", 2)

speak("eduardo")
speak("minx")

# catObj2.speak()

cats = [catObj1, catObj2, catObj3, catObj4]

for i in cats:
    i.speak()