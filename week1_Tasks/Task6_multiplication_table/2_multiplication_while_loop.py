def multiplication(n,num):
    i=1
    while i!=n+1:
        value = i * num
        print(f"\n{num} * {i} = {value}")
        i+=1

def main():
    num = int(input("Enter the muliplication table in number "))
    n =int(input("Enter the number of times wants to multiply"))
    multiplication(n,num)
main()
