# First class function is a language feature where function can be treated as object 
# -> func can be assigned to a variable
# -> func can be passed as an arguments
# -> func can be returned from another func

def square(x):
    return x*x

# 1) assign a function to the variable :

f = square  # Store a reference to the function object.

# () paranthesis meaning here to execute the function 
# here Without paranthesis function object assign to a variable

print(square)
print(f is square)

print(f(5))  # Execute the function and return its result.



# 2) Higher order function :

# Higher-order functions are functions that take one or more functions as arguments or return a function. 
# Higher-order functions are possible because Python supports first-class functions.

# 2a) Functions as arguments :

def add_two(x):
    return x+2

def my_map(func,lst):
    ans=[]
    for i in lst:
        ans.append(func(i))
    return ans

result = my_map(add_two,[0,1,2,3,4,5,6])
print(result)


# 2b) return a function from another function 

# Returning a function: 
# A function returns another function as its return value.

def outer():
    def inner():
        print("Hello")
    return inner

f = outer()
f()


# Closure: 
# A closure is a function object that captures and remembers variables from its enclosing scope, 
# allowing those variables to be accessed even after the outer function has finished executing.

# Closure - 1
def logger(msg):

    def log_message():
        print('hi',msg)

    return log_message

log_hi = logger('python')

log_hi()


# Closure - 2
def html_tag(tag):
    def warp_text(msg):
        print('<{0}> <{1}> <{0}>'.format(tag,msg))
    return warp_text

tag_h1 = html_tag('h1')
tag_p1 = html_tag('p1')
print(tag_h1)
tag_h1('test head line')
tag_h1('another test head line')
