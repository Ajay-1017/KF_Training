# 2) calculator with multiple numbers with if else
def calculator(operation,*args):
    if operation == "sum":
        total = 0
        for num in args:
            total+=num
        return total
    
    elif operation == "sub":
        total = args[0]
        for i in range(1,len(args)):
            total -= args[i]
        return total
    
    elif operation =="mul":
        total = 1
        for num in args:
            total*=num
        return total
    
    elif operation =="div":
        total = args[0]
        for i in range(1,len(args)):
            total /= args[i]
        return total
    
        
    elif operation =="mod":
        total = args[0]
        for i in range(1,len(args)):
            total %= args[i]
        return total
        
    
def main():
    while True:
        operation = input("Enter operation properly sub/sum/mul/div/mod : ")
        op = operation.strip().lower()
        if op == "sub" or op=="sum" or op=="mul" or op =="div" or op =="mod":
            break
        print("enter operation properly from the list sub/sum/mul/div/mod ")

    num = int(input("Enter the number of elements"))
    arr=[]
    for i in range(num):
        value =int(input(f"Enter the number {i+1}: "))
        arr.append(value)
    print(calculator(op,*arr))
main()