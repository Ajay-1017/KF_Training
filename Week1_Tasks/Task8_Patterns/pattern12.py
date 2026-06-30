# pattern 12

# 1......1
# 12....21
# 123..321
# 12344321

def pattern12(n):
    
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(f"{j}",end="")
        
        for space in range(2*n-(i*2)):
            print(".",end="")
        
        for j in range(i,0,-1):
            print(f"{j}",end="")
        print()

pattern12(4)



