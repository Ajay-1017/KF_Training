# pattern 14

# A
# AB
# ABC
# ABCD
# ABCDE

def pattern14(n):
    for i in range(1,n+1):
        k=ord('A')
        for _ in range(1,i+1):
            print(chr(k),end="")
            k+=1
        print()
    
pattern14(5)


            
            



