# 4) Create an Animal hierarchy with different animal types.

# Classes :

# Animal
# Dog
# Cat
# Cow

# Requirements :

# Animal
# Name
# Age

# Each child class should have its own behavior.

# Methods :

# Display animal information.
# Each animal should produce its own sound.
# Demonstrate method overriding by giving each animal a different implementation of the sound method.

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def animal_info(self):
        print("Name :",self.name)
        print("Age :",self.age)

    def sound(self):
        return "some animal sound"
class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)
    
    def sound(self):
        return "bow-bow"

class Cat(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)
    
    def sound(self):
        return "mewo-mewo"
    

class Cow(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)
    
    def sound(self):
        return "moo-moo"


d1 = Dog("shaggy",5)
d1.animal_info()
print(d1.sound())

ca1 = Cat("Blacky",3)
ca1.animal_info()
print(ca1.sound())


co1 = Cow("cowww",7)
co1.animal_info()
print(co1.sound())
