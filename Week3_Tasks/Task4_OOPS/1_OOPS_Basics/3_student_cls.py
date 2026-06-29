# 3) Create a Student class to calculate the average of three subjects

# Using constructor 
class Student:
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def avg(self):
        return (self.m1 + self.m2 + self.m3)//3 


def main():
    m1,m2,m3 = map(int,input("Enter the 3 marks like this format (23 56 78) :").split())
    s1 = Student(m1,m2,m3)
    print(s1.avg())
main()


# Using constructor and *args
class Student:
    def __init__(self,*marks):
        self.marks = list(marks)

    def avg(self):
        return sum(self.marks)/len(self.marks)

def main():
    n = int(input("Enter the subjects : "))
    lst = list(map(int,input(f"Enter the {n} subjects marks : ").split()))
    s1 = Student(*lst)
    print(s1.avg())
main()




# Directly access from the Class
class Student:
    def avg(m1,m2,m3):
        return (m1 +m2 +m3)//3 


def main():
    m1,m2,m3 = map(int,input("Enter the 3 marks like this format (23 56 78) :").split())
    print(Student.avg(m1,m2,m3))
main()