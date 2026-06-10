# pattern 17 


def pattern17(n):
    for i in range(1,n+1):
        k = ord('A')
        for _ in  range(n-i):
            print(".",end="")
        for j in range(2*i-1):
            print(chr(k),end="")
            if j<i-1:
                k+=1
            else:
                k-=1
        for _ in  range(n-i):
            print(".",end="")
        print()

pattern17(4)
            






