# 4) Validate user input for age and salary.

# Method - 1
def main():
        try:
            age = int(input("Enter the age: "))
            if age>0 and age<=120:
                print("age is correct")

            else:
                print("age is wrong")
        except ValueError:
            print("Enter the valid number")
        
        try:
            salary = int(input("Enter the salary: "))

            if salary < 0:
                print("salary is less than zero wrong ")
            else:
                print("salary is correct")
        except ValueError:
            print("Enter the valid number")
             
main()

# Method -2 

def main():
    try:
        age = int(input("Enter the age: "))
        if not (0 <= age <= 120):
            raise ValueError("Age must be between 0 and 120")
        print("age is correct ")


        salary = int(input("Enter the salary: "))
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        print("salary is correct")
    

    except ValueError as e:
        print(e)

main()


