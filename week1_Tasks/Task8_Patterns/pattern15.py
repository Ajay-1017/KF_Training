# pattern 15

# ABCDE
# ABCD
# ABC
# AB
# A


def pattern15(n):
    for i in range(n,0,-1):
        k = ord('A')
        for j in range(i):
            ch = chr(k)
            print(ch,end="")
            k+=1
        print()

pattern15(5)