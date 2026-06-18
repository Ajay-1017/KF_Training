
# 1) Normal function

def display():
    return "hello_world"
print(display())


# 2) Function with parameters and arguments

def add(a,b): # parameters or placeholders
    return a+b
print(1,2) # argumnets or actual values


# 3) Function with default parameters

def add(a,b=5):
    return a+b
print(add(1))

# 4) Higher order function 

# HOF_1 -> Takes function as a parameter 

def gmail(name,domain="gmail.com"):
    return f"{name}@{domain}"

def ymail(name,domain="ymail.com"):
    return f"{name}@{domain}"

def email_builder(name,email_func): # higher order function
    return email_func(name)

print(email_builder("ajay",gmail))


# HOF_2 -> returns functions as its output


def email_builder(domain):
    def build_mail(user_name):
        return f"{user_name}@{domain}"
    return build_mail
gmail = email_builder("@gmail.com")
ymail = email_builder("@ymail.com")

print(gmail("ajay"))


