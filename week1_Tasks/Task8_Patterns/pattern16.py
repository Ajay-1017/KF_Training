# pattern 16

# A
# BB
# CCC
# DDDD
# EEEEE

def pattern16(n):
    k = ord('A')
    for i in range(1,n+1):
        for j in range(i):
            print(chr(k),end="")
        k+=1
        print()
pattern16(5)








 