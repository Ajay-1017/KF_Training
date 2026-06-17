# 1) Print Bob's department.

# 2) Print Charlie's salary.

# 3) Add a new employee emp4.

# 4) Change Alice's salary.

# 5) Print only employee names using a loop.

# 6) Print only departments.

# 7) Print:
#    Alice works in HR
#    Bob works in IT
#    Charlie works in Finance

# 8) Print all salaries.

# 9) Find the employee having the highest salary.

# 10) Find the total salary of all employees.


employees = {
    "emp1": {
        "name": "Alice",
        "department": "HR",
        "salary": 50000
    },
    "emp2": {
        "name": "Bob",
        "department": "IT",
        "salary": 7000000
    },
    "emp3": {
        "name": "Charlie",
        "department": "Finance",
        "salary": 60000
    }
}

# # 1) Print Bob's department.
for emp , details in employees.items():
    if details["name"]=="Bob":
        print(details["department"])
        break

# 2) Print Charlie's salary.
for emp , details in employees.items():
    if details["name"]=="Charlie":
        print(details["salary"])
        break

# 3) Add a new employee emp4.
employees.update(
    { 
    "emp4" : {
        "name": "Ajay",
        "department": "IT",
        "salary": 60000
            }
    }
)
print(employees)

# 4) Change Alice's salary.
for emp , details in employees.items():
    if details["name"]=="Alice":
        details["salary"]=100000
        break
print(employees)

# 5) Print only employee names using a loop

for emp , details in employees.items():
    print(details["name"])


 # 6) Print only departments.   
for emp , details in employees.items():
    print(details["department"]) 

# 7) Print:
#    Alice works in HR
#    Bob works in IT
#    Charlie works in Finance

for emp , details in employees.items():
    print(f"{details['name']} works in {details['department']}")

# 8) Print all salaries.

for emp , details in employees.items():
    print(details["salary"])

# 9) Find the employee having the highest salary.
max = float('-inf')
for emp , details in employees.items():
    if max < details["salary"]:
        max = details["salary"]
        max_name = details["name"]
print(max_name)   


    
# 10) Find the total salary of all employees.
total=0
for emp , details in employees.items():
    total+=details["salary"]
print(total)





