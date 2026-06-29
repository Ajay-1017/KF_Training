class Employee:

    no_of_employees = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@company.com" 
        self.pay = pay
    

    # Regular (instance) methods automatically receive the instance (self)
    # as the first argument.
    def raise_pay(self):
        self.pay = int(self.pay) * self.raise_amount


    # Class methods automatically receive the class (cls)
    # as the first argument.
    @classmethod
    def raise_amount_change(cls,amount):
        cls.raise_amount = amount


    # Alternative constructor
    @classmethod 
    def from_string(cls,emp_str):
        first , last , pay = emp_str.split('-')
        return cls(first,last,pay)


    # Static methods do not receive self or cls automatically.
    # They behave like regular functions placed inside the class.
    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday()==6:
            return False
        return True


e1 = Employee("Ajay","Balu",20000) 
e2 = Employee('Aravinth','Seelan',30000) 

# Changing the class variable using a class method
Employee.raise_amount_change(1.04)

print(e1.raise_amount)
print(Employee.raise_amount)


# Creating an object by manually splitting the string
emp_str_1 = "Ajay-Balu-20000"
emp_str_2 = "Aravinth-Seelan-30000"

first , last , pay = emp_str_1.split('-')
emp_1 = Employee(first , last , pay)
print(emp_1.first)
print(emp_1.pay)


# Creating an object using the alternative constructor (class method)
emp_1  = Employee.from_string(emp_str_1)
print(emp_1.first)
print(emp_1.pay)


# Calling the static method
import datetime
my_date = datetime.date(2026,6,29)
print(Employee.is_work_day(my_date))
