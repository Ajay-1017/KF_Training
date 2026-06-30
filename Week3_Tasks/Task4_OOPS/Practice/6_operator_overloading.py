


class Student:

    def __init__(self,m1,m2):
        self.m1= m1
        self.m2 = m2

    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        m3 = Student(m1,m2)
        return m3
    
    def __gt__(self,other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2

        if s1 > s2:
            return True
        else:
            return False
        
    def __str__(self):
        return f"{self.m1},{self.m2}"

std1 = Student(50,62)
std2 = Student(50,61)

total = std1 + std2

if std1>std2:
    print("std1 wins")
else:
    print("std2 wins")

print(total.m1)
print(total.m2)



a=9
print(a)
print(a.__str__()) # same as above

print(std1)
print(std2)




    