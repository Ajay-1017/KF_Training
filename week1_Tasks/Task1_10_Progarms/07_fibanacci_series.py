def fibanacci_series(n):
    a=0
    b=1
    ans=[a,b]
    if n == 0:
        return [0]
    elif n == 1:
        return [0,1]
    
    for _ in range(n-2):
        c = a+b
        ans.append(c)
        a = b 
        b = c
    return ans

def main():
    n = int(input("enter number upto the series u want : "))
    print(fibanacci_series(n))
main()

