
class Employee: # class (blue print of creating objects)

    no_of_employees = 0
    raise_amount  = 1.04  # Class variable

    def __init__(self,first,last,pay): # constructor (initializer)

        # Instance Attributes or Instance variables
        self.first = first 
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.no_of_employees +=1

    # Regular Methods
    def full_name(self):
        return '{0} {1}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

e1 = Employee("Ajay","Balu",20000) # object (instance of a employee class)  
e2 = Employee('Aravinth','Seelan',30000) # another object (constructor is called automatically during object creation)

print(Employee.no_of_employees)

Employee.raise_amount = 1.05 
e1.raise_amount = 1.04
print(e1.__dict__)

print(Employee.raise_amount)
print(e1.raise_amount)
print(e2.raise_amount)

