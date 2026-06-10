# Pattern 5 

# *****
# ****
# ***
# **
# *

# Method-1 (using reverse loop)
def pattern5(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end="")
        print()

pattern5(5)

    
# Method-2 (using forward loop)

def pattern5(n):
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print("*",end="")
        print()

pattern5(5)