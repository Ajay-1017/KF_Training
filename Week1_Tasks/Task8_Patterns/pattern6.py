# Pattern 6

# 12345
# 1234
# 123
# 12
# 1

def pattern6(n):
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print(f"{j}",end="")
        print()

pattern6(5)
