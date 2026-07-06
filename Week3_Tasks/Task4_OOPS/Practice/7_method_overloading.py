
# since there is no method overloading in python
# make a logic to work like method overloading
class Student:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a
        return s

s1 = Student()
print(s1.add(1,2))
print(s1.add(1,2,3))

