

# Create lambda functions for:

# Addition of two numbers.
# Finding square of a number.
# Finding maximum of two numbers.
# Checking even or odd.
# Converting text to uppercase.


# 1)Addition of two numbers.
add = lambda a,b: a+b 
print(add(1,2))

# 2)Finding square of a number.
square = lambda x:x**2
print(square(2))

# 3)Finding maximum of two numbers.
max_number = lambda a,b : a if a>b else b 
print(max_number(10,12))

# 4)Checking even or odd.
even_odd = lambda num : "even" if num%2==0 else "odd"
print(even_odd(4))

# 5)Converting text to uppercase.
upper_case = lambda str : str.upper()
print(upper_case("hello"))



