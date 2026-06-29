# 3) Build a School Management hierarchy with Person, Teacher, and Student.

# Classes :

# Person
# Teacher
# Student

# Requirements :

# Person :
# Name
# Age

# Teacher :
# Subject
# Salary

# Student :
# Roll number
# Grade

# Methods :

# Show basic information.
# Teacher should display subject and salary.
# Student should display roll number and grade.


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print("Name :",self.name)
        print("Age :",self.age)
    

class Teacher(Person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject = subject
        self.salary = salary
    
    def display_teacher_info(self):
        self.display_person_info()
        print("subject :",self.subject)
        print("salary :",self.salary)
    
        
class Student(Person):
    def __init__(self,name,age,roll_no,grade):
        super().__init__(name,age)
        self.roll_no = roll_no
        self.grade = grade
    
    def display_student_info(self):
        self.display_person_info()
        print("Roll no :",self.roll_no)
        print("Grade :",self.grade)


p1 = Person("Ajay",21)   
p1.display_person_info()
print('*'*50)

t1 = Teacher("balaji",45,"Electron device",80000)   
t1.display_teacher_info()
print('*'*50)

s1 = Student("Ajay",21,7,"O")   
s1.display_student_info()
print('*'*50)






























