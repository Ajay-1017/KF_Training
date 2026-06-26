
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
                try:
                    result/=num
                except ZeroDivisionError:
                    return "Division by zero is not possible"
            case "%":
                result%=num
            case "_":
                return "invalid operator"
    return result

    
    
        





        




