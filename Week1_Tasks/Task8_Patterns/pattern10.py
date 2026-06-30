# pattern 10


# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

def pattern10(n):
    for i in range(1,2*n):
        if i<=n:
            star = i
        else:
            star = i - (i-n)*2

        for _ in range(star):
            print("*",end="")
        print()

pattern10(5)