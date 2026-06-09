def multiplication(n,num):
    for i in range(1,n+1):
        value = num * i
        print(f"\n{num} * {i} = {value}")
    
def main():
    num = int(input("Enter the muliplication table in number "))
    n =int(input("Enter the number of times wants to multiply"))
    multiplication(n,num)
main()
