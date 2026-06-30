# 1) Create different Shape classes with their own area calculation.

# What to do
# Create a common parent class: Shape

# Create child classes:
# Circle
# Rectangle
# Triangle

# Each class should calculate its own area differently.
# Use the same method name for area calculation in all classes.


# 1) Method overriding 

class Shape:
    def area(self):
        pass
 
class Circle(Shape):
    def area(self,r):
        return 3.14 *(r**2)

class Rectangle(Shape):
    def area(self,l,b):
        return l*b

class Triangle(Shape):
    def area(self,b,h):
        return 0.5*b*h
    

s1 = Shape()
c1 = Circle()
r1 = Rectangle()
t1 = Triangle()

print(s1.area())
print(c1.area(4))
print(r1.area(5,10))
print(t1.area(3,10))

print('='*50)

# 2) Duck Typing 
 
class Circle:
    def area(self,r=5):
        return 3.14 *(r**2)

class Rectangle:
    def area(self,l=5,b=10):
        return l*b

class Triangle:
    def area(self,b=3,h=10):
        return 0.5*b*h
    
def caluclate_area(obj):
    return obj.area()

cir = Circle()
rec = Rectangle()
tri = Triangle()

print(caluclate_area(cir))
print(caluclate_area(rec))
print(caluclate_area(tri))

