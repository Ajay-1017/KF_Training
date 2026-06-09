def calculator(expression):

    arr = expression.split()
    result = float(arr[0])

    for i in range(1,len(arr),2):
        op = arr[i]
        num = float(arr[i+1])

        match op :
            case "+":
                result+=num
            case "-":
                result-=num
            case "*":
                result*=num
            case "/":
                if num==0:
                    return "division by zero is not possible"
                result/=num
            case "%":
                result%num
    return result

def main():
    while True:
        expression = input("Enter the expression in this format 5 + 8 - 10 : ")
        
        arr = expression.split()
        valid = True

        if len(arr) % 2 == 0:
            valid = False



        for i in range(0,len(arr),2):
            try:
                float(arr[i])
            except ValueError:
                valid = False
                break

        
        for i in range(1,len(arr),2):
            if arr[i] not in ('+','-','*','/','%'):
                valid = False
        
        if not valid:
            print("enter the expression properly in this format 5 + 8 - 10 :  ")
        else:
            break
    
    print(calculator(expression))

main()
    
    
        





        




