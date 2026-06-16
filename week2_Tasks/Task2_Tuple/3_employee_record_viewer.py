import re
ID = 0
NAME = 1
AGE = 2
DEPT= 3
SAL= 4

def menu():
    print("\n===== EMPLOYEE RECORD VIEWER =====")
    print("1. Display All Employees")
    print("2. Search by ID")
    print("3. Search by Name")
    print("4. Department-wise Count")
    print("5. Highest Salary Employee")
    print("6. Lowest Salary Employee")
    print("7. Average Salary")
    print("8. Employees Older Than Given Age")
    print("9. Employees by Department")
    print("10. Total Employees")
    print("11. Salary Above Amount")
    print("12. Sort Employees by department")
    print("13. Duplicate Names")
    print("14. Name Starts With Letter")
    print("15. Exit")


def searchByID(employees,n):
    for emp in employees:
        if emp[ID]==n:
            return emp
    return -1

def SearchByName(employees,name):
    ans=[]
    for emp in employees:
        if emp[NAME].upper()==name.upper():
            ans.append(emp)
    return ans 

def departmentCount(employees,dept):

    # Method-1 normal count logic 

    count=0
    for emp in employees:
        if emp[DEPT]==dept:
            count+=1
    return count

    # Method-2 using count method

    # department = tuple(emp[DEPT] for emp in employees)
    # cnt = department.count(dept)
    # return cnt

def highest_sal(employees):

    # Method-1 using generator and max

    # ans=[]
    # max_salary = max(emp[SAL] for emp in employees)
    # for emp in employees:
    #     if emp[SAL] == max_salary:
    #         ans.append(emp)
    # return ans

    # Method-2 using for loop

    max_salary = float("-inf")
    ans = []

    for emp in employees:
        if emp[SAL] > max_salary:
            max_salary = emp[SAL]
            ans = [emp]
        elif emp[SAL] == max_salary:
            ans.append(emp)
    return ans
    


def lowest_sal(employees):
    min_salary = float("inf")
    ans = []

    for emp in employees:
        if emp[SAL] < min_salary:
            min_salary = emp[SAL]
            ans = [emp]
        elif emp[SAL] == min_salary:
            ans.append(emp)
    return ans

def Average_sal(employees):
    if len(employees)==0:
        return 0

    # Method-1
    return sum(emp[SAL] for emp in employees)/len(employees)

    # Method - 2
    # total=0
    # for emp in employees:
    #     total+=emp[SAL]
    # return (total/len(employees))

def employeesOld(employees,age):
    ans=[]
    for emp in employees:
        if emp[AGE]>age:
            ans.append(emp)
    return ans

def employeesByDept(employees,dept):
    ans=[]
    for emp in employees:
        if dept == emp[DEPT]:
            ans.append(emp)
    return ans


def salary_above(employees, amount):
    ans = []

    for emp in employees:
        if emp[SAL] > amount:
            ans.append(emp)

    return ans

def sortBydept(employees):
    # Bubble sort 
    temp = list(employees)

    for i in range(len(temp)-1):
        for j in range(len(temp)-i-1):
            if temp[j][DEPT] > temp[j+1][DEPT]:
                temp[j], temp[j+1] = temp[j+1], temp[j]

    return temp

def duplicate_names(employees):
    freq = {}

    for emp in employees:
        freq[emp[NAME]] = freq.get(emp[NAME], 0) + 1

    ans = []

    for emp in employees:
        if freq[emp[NAME]] > 1:
            ans.append(emp)

    return ans

def nameStarts(employees, ch):

    # Method - 1 (regex)
    # ans = []

    # for emp in employees:
    #     if re.match(f"{ch}", emp[NAME]):
    #         ans.append(emp)

    # return ans

    # Method-2 
    ans = []

    for emp in employees:
        if emp[NAME].upper().startswith(ch.upper()):
            ans.append(emp)

    return ans



 
def main():
    employees = (
    (101, "Ajay", 23, "IT", 40000),
    (102, "Arun", 25, "HR", 52000),
    (103, "Kumar", 28, "ECE", 48000),
    (104, "Priya", 24, "IT", 60000),
    (105, "Divya", 30, "HR", 55000),
    (106, "Ajay", 27, "ECE", 47000),
    (107, "Vijay", 22, "IT", 40000),
    (108, "Sneha", 29, "CSE", 65000),
    (109, "Arun", 26, "CSE", 70000),
    (110, "Meena", 31, "HR", 70000)
)
    

    while True:
        menu()
        try:
            choice = int(input("\nEnter choice: "))
        except ValueError:
            print("Invalid input")
            continue
    
        match choice:
            case 1:
                for emp in employees:
                    print(emp)
            case 2:
                while True:
                    try:
                        n = int(input("\nEnter the id : "))
                        emp_id = searchByID(employees, n)

                        if emp_id != -1:
                            break

                        print("Employee ID is incorrect")
                    except ValueError:
                        print("Enter a valid number")
                print(f"\nEmployee ID {n} details : {emp_id}")

                
                
            case 3:
                while True:
                    n = input("\nEnter the name :")
                    emp_name = SearchByName(employees,n)
                    if emp_name!=[]:
                        break
                    print("\nemployee name is incorrect please enter the correct employee name ")
                
                print(f"\n{len(emp_name)} employee is found")
                for emp in emp_name:
                    print(f"\nemployee {emp[ID]} details : {emp}")
            
            case 4:
                while True:
                    dept = input("\nEnter the department (ECE/IT/HR/CSE): ")
                    dept = dept.upper()
                    if dept in ("ECE","IT","HR","CSE"):
                        break
                    print("\nEnter the dept name properly")

                cnt=departmentCount(employees,dept)
                print(f"Department {dept} count : {cnt}")

            case 5:
                print("\nhighest salary :")
                high_sal = highest_sal(employees)
                for sal in high_sal:
                    print(sal)
            
            case 6:
                print("\nlowest salary :")
                low_sal = lowest_sal(employees)
                for sal in low_sal:
                    print(sal)

            case 7:
                print("\naverage_sal:",Average_sal(employees))

            case 8:
                while True:
                    try:
                        age = int(input("Enter the age: "))
                        if age>=0 and age<=120:
                            break
                        print("enter the correct age")
                    except ValueError:
                        print("Enter the valid number")
                
                older_employees  = employeesOld(employees,age)
                if older_employees !=[]:
                    for age in older_employees :
                        print(age)
                else:
                    print("no record in those age")
                
            case 9:
                while True:
                    dept = input("\nEnter the department (ECE/IT/HR/CSE): ")
                    dept = dept.upper()
                    if dept in ("ECE","IT","HR","CSE"):
                        break
                    print("\nEnter the dept name properly")

                print(f"\n{dept} employees details:")
                emp = employeesByDept(employees,dept)

                for e in emp:
                    print(e)


            case 10:
                print(f"\n total employees : {len(employees)}")

            case 11:
                while True:
                    try:
                        amount = int(input("Enter the amount: "))
                        break
                    except ValueError:
                        print("Enter a valid amount")

                emp_list = salary_above(employees, amount)

                if emp_list:
                    for emp in emp_list:
                        print(emp)
            
                else:
                    print("No employee salary above this amount")
                    
            case 12:
                sorted_employees = sortBydept(employees)

                for emp in sorted_employees:
                    print(emp)

            case 13:
                print("\nEmployees details with same names ")
                dup = duplicate_names(employees)
                if dup:
                    for i in dup:
                        print(i)
                else:
                    print("No duplicate names")

            case 14:
                while True:
                    ch = input("Enter the charcter names start :")
                    if len(ch)==1 and ch.isalpha():
                        break
                    print("Enter the charcter properly")
                    
                name = nameStarts(employees,ch.upper())

                if name:
                    for i in name:
                        print(i)
                else:
                    print("No employee found")

            case 15:
                print("------------exit-----------")
                break
            
            case _:
                print("Invalid choice")
main()
