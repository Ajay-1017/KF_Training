# 1) Create an Employee class with employee details and display them.

class Employee: # class (blue print of creating objects)

    def __init__(self,first,last,pay): # constructor (initializer)

        # Instance Attributes or Instance variables
        self.first = first 
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    # Class Method
    def full_name(self):
        return '{0} {1}'.format(self.first,self.last)

e1 = Employee("Ajay","Balu",20000) # object (instance of a employee class)  
e2 = Employee('Aravinth','Seelan',30000) # another object (constructor is called automatically during object creation)

print(e1.email) 
print(e2.email)
print(e1.full_name())
print(Employee.full_name(e2))