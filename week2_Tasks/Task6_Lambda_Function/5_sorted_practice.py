
# Sort numbers ascending.
# Sort numbers descending.
# Sort strings alphabetically.
# Sort strings by length.
# Sort tuples based on one of their elements.


# 1)Sort numbers ascending.
lst =[1,-2,3,-4,5,-6,7,8]
print(sorted(lst))

# 2)Sort numbers descending.
lst =[1,-2,3,-4,5,-6,7,8]
print(sorted(lst,reverse = True))

# 3)Sort strings alphabetically.
names = ["xavier","ajay","aaravinth","balaji","vignesh"]
print(sorted(names))

# 4)Sort strings by length.
names = ["xavier","ajay","aaravinth","balaji","vignesh"]
print(sorted(names , key = lambda x : len(x),reverse=True))

# 5)Sort tuples based on one of their elements.
data = [(3, 100), (1, 200), (2, 150)]
print(sorted(data,key=lambda x: x[0],reverse=True))
