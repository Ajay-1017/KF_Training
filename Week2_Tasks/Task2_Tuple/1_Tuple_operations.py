# 1) ITERATING THE TUPLE
a=(1,"a","hello",[1,2,3],1,1,1)

for i in a:
    print(i)


# 2) EMPTY TUPLE
b=()
print(b)


# 3) TUPLE INSIDE LIST IS MUTABLE
a[3][2]=1
print(a)


# 4) TUPLE METHODS (index & count)
print(a.index("hello"))
print(a.count(1))

# 5) Packing and unpacking

packing=(1,"a","hello",[1,2,3],1,1,1) #packing
print(packing)

name, age,department = ("ajay",21,"ece")
print ("name:",name)
print("age:",age)
print("dept:",department)

