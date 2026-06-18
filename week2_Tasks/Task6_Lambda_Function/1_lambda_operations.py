

# lambda 
# syntax -> lambda parametes : valid expression

add = lambda a,b:a+b
print(add(1,2)) 

square = lambda x : x*x
print(square(5))


# map function -> To map every element in an iterable 
# syntax -> map(function , iterable)

lst =[1,2,3,4]
print(list(map(lambda x: x**2 ,lst))) # square every elements


# filter function -> To filter elements from an iterable 
# syntax -> filter(function , iterable)

lst = [1,2,3,4]
print(list(filter(lambda x: x%2==0 , lst))) # even number from lst

# sorted() fuction 
lst=[9,3,7,5,8,6,7]
print(sorted(lst,reverse = True))
print(lst)

#sort
lst=[9,3,7,5,8,6,7]
lst.sort()
print(lst)


# reduce function -> it returns only one value
from functools import reduce
lst =[1,2,4,4,5,6,7,8,9,0]
total = reduce(lambda a,b : a+b , lst) 
print(total)

max_number = reduce(lambda a,b : a if a>b else b,lst )
print (max_number)