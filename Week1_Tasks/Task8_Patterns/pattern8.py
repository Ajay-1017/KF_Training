# Pattern 8

# (.) -> space

# *********
# .*******.
# ..*****..
# ...***...
# ....*....

def pattern8(n):
    for i in range(1,n+1):
        for _ in range(i-1):
            print(".",end="")
        for _ in range(2*n-(2*i-1)):
            print("*",end="")
        for _ in range(i-1):
            print(".",end="")
        print()

pattern8(5)


