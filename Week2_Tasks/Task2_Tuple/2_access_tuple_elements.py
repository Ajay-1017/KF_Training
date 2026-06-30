# ACCESSING TUPLE ELEMENTS

std=(
    (1,"bob",20,"ece"),
    (2,"akshay",21,"ece"),
    (3,"kishore",22,"cs"),
    (4,"kumar",23,"it"),
    (5,"balaji",24,"ece"),
    (6,"ajay",25,"ece")
    )

# Print all student records.
print(std)

# Print the first student.
print(std[0])


# Print the name of the third student.
print(std[2][1])

# Print the age of the last student.
print(std[-1][2])


# Use negative indexing to access a student.
print(std[-2])


# Unpack one student's tuple into variables like id, name, age, and dept.
id ,name,age,dept = std[2]
print(id,name,age,dept)


# TUPLE METHODS(COUNT & INDEX)

# Find how many students belong to "ece" using count().
department = tuple(s[3] for s in std)
print(department.count("ece"))


# Find the position of a particular student tuple using index().
for s in std:
    if s[1]=="ajay":
        print(std.index(s))


