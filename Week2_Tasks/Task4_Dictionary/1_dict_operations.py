# Key-Value pairs 	
# Access values using keys 	
# get()
# keys()
# values()
# items()
# update()


person = {
    "name": "John",
    "age": 30,
    "is_employed": True,
    "skills": ["Python", "SQL", "Excel"]
}

# 1) ACCESS VALUES USING KEYS 	
print(person["age"])
print(person["skills"][1])

# 2) get()
print(person.get("age"))
print(person.get("dept")) #If not in dict it will get() Gives none whereas normal getting method gives as error

# 3) keys()
print(person.keys()) # It takes no arguments

# 4) values()
print(person.values())  # It takes no arguments

# 5)items()
print(person.items()) # It takes no arguments

# 6)update()
person.update({"gender":"male"})
print(person)


company = {
    "employee1": {
        "name": "Alice",
        "department": "HR"
    },
    "employee2": {
        "name": "Bob",
        "department": "IT"
    },
    "employee3": {
        "name": "Charlie",
        "department": "Finance"
    }
}

for emp , details in company.items():
    print(emp , details["department"])


