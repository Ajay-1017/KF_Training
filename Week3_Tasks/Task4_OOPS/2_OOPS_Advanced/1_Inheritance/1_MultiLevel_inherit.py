
# 1) Create a Person → Employee → Manager inheritance hierarchy. 

# Classes :

# Person
# Employee
# Manager

# Requirements :

# Person should store:
# First name
# Last name
# Age

# Employee should inherit from Person and additionally store:
# Employee ID
# Salary
# Department

# Manager should inherit from Employee and additionally store:
# Team size
# Bonus

# Methods :

# Display personal information.
# Display employee information.
# Display manager information.
# Calculate total salary after adding bonus.

class Person:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        self.email = first + '.'+ last[0] +'@company.com'
    
    def full_name(self):
        return self.first +" "+ self.last
    
    def display_Person_info(self):
        print("Full_name :",self.full_name())
        print("Age :",self.age)
        print("email",self.email)



class Employee(Person):

    def __init__(self,first,last,age, emp_id , salary , department):
        super().__init__(first,last,age)
        self.emp_id =emp_id
        self.salary = salary
        self.department = department

    def display_employee_info(self):
        self.display_Person_info()
        print("Employee_id :",self.emp_id)
        print("Department :",self.department)
        print("salary:",self.salary)


class Manager(Employee):
    def __init__(self,first,last,age,emp_id,salary,department,employees=None):
        super().__init__(first,last,age,emp_id,salary,department)
        
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employees(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employees(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)       

    def team_size(self):
        return len(self.employees)
    
    def display_employees(self):
        if not self.employees :
            print("no employees reporting to this manager")
        for emp in self.employees:
            print("-->",emp.full_name())

    def add_bonus(self,emp,amount): # Manager gives bonus to employee 
        if emp in self.employees:
            emp.salary += amount

    def display_manager_info(self):
        self.display_employee_info()
        


# Person object
p1 = Person("Ajay","Balu",21)
p1.display_Person_info()
print("-"*50)

# Employee objects
emp1 = Employee("Aravinth","Seelan",21,101,30000,"Developer")
emp2 = Employee("Vijaya","Balu",52,24,100000,"HR")
emp1.display_employee_info()
print("-"*50)


# Manager object
mgr1 = Manager("Priyanka","Balu",28,34,80000,"Manager",[emp1])
print(mgr1.email)
mgr1.add_employees(emp2)
mgr1.display_employees()
print("Team_size :",mgr1.team_size())
# mgr1.remove_employees(emp1)
# mgr1.display_employees()


# Manager adding bonus to the employee
print(emp1.salary)   
mgr1.add_bonus(emp1,1000)
print(emp1.salary)
print("-"*50)

# displaying Manager's details
mgr1.display_manager_info()