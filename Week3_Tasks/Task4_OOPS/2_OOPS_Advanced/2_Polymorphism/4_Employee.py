# 4) Create Different Employee Types with Different Salary Calculation Methods

# What to do

# Create a common parent class:
# Employee

# Create child classes:
# FullTimeEmployee
# PartTimeEmployee
# Freelancer

# Requirements:
# Store employee details.
# Each employee type should calculate salary differently.
# Use the same salary calculation method name in all classes.
# Display employee details and salary.


class Employee:
    def __init__(self,name,age,base_salary):
        self.name  = name
        self.age = age
        self.base_salary = base_salary

    def employee_details(self):
        print("name :",self.name)
        print("age :",self.age)
        print("base_salary :",self.base_salary)

    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self,name,age,base_salary):
        super().__init__(name,age,base_salary)
    def calculate_salary(self):
        return self.base_salary + 10000

    def employee_details(self):
        super().employee_details()
        print("salary :",self.calculate_salary())


class PartTimeEmployee(Employee):
    def __init__(self,name,age,base_salary):
        super().__init__(name,age,base_salary)

    def calculate_salary(self):
        return self.base_salary + 5000
    
    def employee_details(self):
        super().employee_details()
        print("salary :",self.calculate_salary())

class Freelancer(Employee):
    def __init__(self,name,age,base_salary):
        super().__init__(name,age,base_salary)

    def calculate_salary(self):
        return self.base_salary + 1000

    def employee_details(self):
        super().employee_details()
        print("salary :",self.calculate_salary())

emp = Employee("ajay",21,30000)
emp.employee_details()
print('='*50)

full = FullTimeEmployee("ajay",21,25000)
print(full.calculate_salary())
full.employee_details()
print('='*50)

part = PartTimeEmployee("ajay",21,25000)
print(part.calculate_salary())
part.employee_details()
print('='*50)

free = Freelancer("ajay",21,25000)
print(free.calculate_salary())
free.employee_details()
