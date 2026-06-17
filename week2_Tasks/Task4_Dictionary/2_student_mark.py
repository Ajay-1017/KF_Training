# 1) Print the mark in Science.

# 2) Print all subject names.

# 3) Print all marks.

# 4) Print all key-value pairs.

# 5) Add a new subject "History" with mark 88.

# 6) Change the English mark to 97.

# 7) What happens if you do:
#    print(marks["Physics"])

# 8) What does this return?
#    print(marks.get("Physics"))

# 9) Write a loop to print:
#    Math 90
#    Science 85
#    English 95
#    History 88

# 10) Find the total of all marks.

marks = {
    "Math": 90,
    "Science": 85,
    "English": 95
}

# 1) Print the mark in Science.
print(marks["Science"])

# 2) Print all subject names.
for sub in marks:
    print(sub)

# 3) Print all marks
for mark in marks.values():
    print(mark)


# 4) Print all key-value pairs.

for kv in marks:
    print(kv,marks[kv])

for key , value in marks.items():
    print(key,value)


# 5) Add a new subject "History" with mark 88.
marks["History"]=88
print(marks)

# 6) Change the English mark to 97.

marks.update({"English":97})
print(marks)

# 7) What happens if you do:
# print(marks["Physics"])
# There is no subject physics as key it will give key error

# 8) What does this return?
# print(marks.get("Physics"))
# return none

# 9) Write a loop to print:
#    Math 90
#    Science 85
#    English 95
#    History 88

for key , value in marks.items():
    print(key,value)

# 10) Find the total of all marks.
total=0
for sub , mark in marks.items():
    total+=mark
print(total)

for mark in marks.keys():
    print(mark)