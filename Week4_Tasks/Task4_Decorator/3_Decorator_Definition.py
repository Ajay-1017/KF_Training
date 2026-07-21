
# A decorator is a higher-order function that takes another function, 
# adds extra behavior without modifying the original function's source code, and returns a new function.

print("\n-------------------------Decorator function------------------------")

# 1) Decorator function 
def decorator_function(original_function):

    def wrapper_function(*args):
        print("wrapper function execute before {}".format(original_function.__name__))
        return original_function(*args)
    
    return wrapper_function




@decorator_function # same as this -> display = decorator_function(display) 
def display():
    print("welcome to decorator programming ")
display()

# display = decorator_function(display)
# display() 

print("*"*50)

@decorator_function
def display_info(name,age):
    print("name = ",name)
    print('age = ',age)
display_info("ajay",21)

# display_info = decorator_function(display_info)
# display_info("ajay",21)


print("\n-------------------------Decorator class------------------------")
# 2) Decorator class

class Decorator_class:
    def __init__(self,original_func):
        self.original_func = original_func

    def __call__(self,*args):
        print("call mehod execute before {}".format(self.original_func.__name__))
        return self.original_func(*args)
    
@Decorator_class # same as this -> display = decorator_function(display) 
def display():
    print("welcome to decorator programming ")
display()

# display = decorator_function(display)
# display() 

print("*"*50)

@Decorator_class
def display_info(name,age):
    print("name = ",name)
    print('age = ',age)
display_info("ajay",21)