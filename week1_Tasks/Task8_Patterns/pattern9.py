# Pattern 9 

# ....*....
# ...***...
# ..*****..
# .*******.
# *********
# *********
# .*******.
# ..*****..
# ...***...
# ....*....

# Method - 1 (combining upper and lower part with two for loops)

def pattern9(n):
    for i in range(1,n+1):
        for _ in range(n-i):
            print(".",end="")
        for _ in range(2*i-1):
            print("*",end="")
        for _ in range(n-i):
            print(".",end="")
        print()
    
    for i in range(1,n+1):
        for _ in range(i-1):
            print(".",end="")
        for _ in range(2*n - (2*i-1)):
            print("*",end="")
        for _ in range(i-1):
            print(".",end="")
        print()

pattern9(5)

# Method - 2 (single for loop with if else condition )

def pattern9(n):

    for i in range(1,2*n+1):
        if i<=n:
            space = n-i
            star = 2*i-1
        else:
            space = i-n-1
            star = 2*n -((i-n)*2-1)
        
        for _ in range(space):
            print(".",end="")
        for _ in range(star):
            print("*",end="")
        for _ in range(space):
            print(".",end="")

        print()
pattern9(5)



# Method-3 (same as above but without repeating the center part)

# ....*....
# ...***...
# ..*****..
# .*******.
# *********
# .*******.
# ..*****..
# ...***...
# ....*....


def pattern9(n):

    for i in range(1,2*n):
        if i<=n:
            space = n-i
            star = 2*i-1
        else:
            space = i-n
            star = 2*n -((i-n)*2+1)
        
        for _ in range(space):
            print(".",end="")
        for _ in range(star):
            print("*",end="")
        for _ in range(space):
            print(".",end="")

        print()
pattern9(5)


            





    



