#  simple calculator with two numbers only 

def calculator(operation,a,b):
    if operation == "sum":
        return a+b
    elif operation == "sub":
        return a-b
    elif operation =="mul":
        return a*b
    elif operation =="div":
        return a/b
    elif operation =="mod":
        return a%b
    
def main():
    while True:
        operation = input("Enter operation properly sub/sum/mul/div/mod : ")
        op = operation.strip().lower()
        if op == "sub" or op=="sum" or op=="mul" or op =="div" or op =="mod":
            break
        print("enter operation properly from the list sub/sum/mul/div/mod ")

    a = int(input("enter number 1 : "))
    b = int(input("enter number 2: "))
    print(calculator(op,a,b))
main()