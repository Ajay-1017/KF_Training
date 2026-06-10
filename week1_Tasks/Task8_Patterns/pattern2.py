# Pattern 2

# *
# **
# ***
# ****
# *****

def pattern2(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end="")
        print()
        
pattern2(5)

