def fact(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact

def main():
    num = int(input("enter any number : "))
    print(fact(num))
main()


        