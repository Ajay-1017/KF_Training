# pattern 19

# E
# DE
# CDE
# BCDE
# ABCDE

def pattern19(n):
    k = ord('A')+(n-1)
    for i in range(1,n+1):
        for _ in range(i):
            print(chr(k),end="")
            k+=1
        k-=i+1
        print()
         
pattern19(5)

