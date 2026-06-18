
# Extract even numbers.
# Extract odd numbers.
# Find positive numbers.
# Filter names starting with a specific letter.
# Select numbers greater than a given value.

# 1)Extract even numbers.
lst =[1,-2,3,-4,5,-6,7,8]
print(list(filter(lambda x : x%2==0,lst)))

# 2)Extract odd numbers.
print(list(filter(lambda x : x%2!=0,lst)))

# 3)Find positive numbers.
print(list(filter(lambda x : x>0,lst)))

# 4)Filter names starting with a specific letter.
names = ["ajay","aravinth","balaji","vignesh"]
print(list(filter(lambda word : word[0]=="a",names)))

# 5)Select numbers greater than a given value.
print(list(filter(lambda x : x>3,lst)))
