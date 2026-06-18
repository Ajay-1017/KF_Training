
# Convert a list of numbers into squares.
# Convert temperatures from Celsius to Fahrenheit.
# Convert names to uppercase.
# Find lengths of strings.
# Add two lists element-wise.


# 1) Convert a list of numbers into squares.

lst = [1,2,3,4,5,6]
square = list(map(lambda x: x**2 , lst))
print(square)

# 2) Convert temperatures from Celsius to Fahrenheit.
# F = C * 9/5 + 32
# c = f - 32 * 5/9

temperatures = [102,97,32,45,56,68]
print(list(map(lambda x: f"{x*9/5+32:.2f}", temperatures)))

# 3) Convert names to uppercase.

names = ["ajay","aravinth","balaji","vignesh"]
print(list(map(lambda name : name.upper(),names)))

# 4) Find lengths of strings.
names = ["ajay","aravinth","balaji","vignesh"]
print(list(map(lambda name : len(name),names)))

# 5) Add two lists element-wise.
a = [1,2,2,3,4,5,6]
b = [3,2,2,1,0,-1,-2]

print(list(map(lambda a,b :a+b,a,b)))