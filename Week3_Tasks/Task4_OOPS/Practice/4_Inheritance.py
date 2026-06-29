
class Employee:     
    raise_amount = 1.05
    def __init__(self,first,last,pay): 

        self.first = first 
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

   
    def full_name(self):
        return '{0} {1}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)

# sub class inherited from Parent Class (Employee)
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self,first,last,pay,prog):
        # Call the parent class (Employee) constructor to initialize inherited attributes.
        super().__init__(first,last,pay)
        # Employee.__init__(self,first,last,pay) # same as super()
        self.prog = prog


# another sub class inherited from parent class (Employee)
class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_employees(self):
        for emp in self.employees:
            print("-->",emp.full_name())


dev1 = Developer("Ajay","Balu",20000,"PYTHON") # object (instance of a employee class)  
dev2 = Developer('Aravinth','Seelan',30000,"JAVA") # another object (constructor is called automatically during object creation)

mng1 = Manager("Priyanka","Balu",45000,[dev1])
# help() -> Show all available methods, attributes, and documentation of dev1.
# print(help(dev1)) 


# Changing the raise amount of parent_class in sub_class and see the changes
# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)


# testing the developer sub class
# print(dev1.email)
# print(dev1.prog)


# testing the manager sub class
# print(mng1.email)
# mng1.add_employee(dev2)
# mng1.remove_employee(dev1)
# mng1.print_employees()


# isinstance and issubclass returns True or False
print(isinstance(mng1,Manager))
print(isinstance(mng1,Employee))
print(isinstance(mng1,Developer)) 

print(issubclass(Manager,Employee))
print(issubclass(Employee,Manager))
