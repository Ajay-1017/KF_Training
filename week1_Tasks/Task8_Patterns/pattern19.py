# pattern 19 

# *           * 
# *           * 
# *           * 
# * * * * * * * 
# *           * 
# *           * 
# *           * 


# Method - 1 (Nested Loops)
def patternH(n):
    mid = n // 2

    for i in range(n):
        for j in range(n):
            if j == 0 or j == n - 1 or i == mid:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

patternH(5)


# Method - 2 (optimzed version)

def patternH(n):
    mid = n // 2

    for i in range(n):
        if i == mid:
            print("* " * ((2*n)//2))
        else:
            print("*" + " " * (2*n-3) + "*")

patternH(7)