# 3) calculator with multiple numbers with match case

def calculator(operation,*args):

    match operation:
        case "sum":
            total = 0
            for num in args:
                total+=num
            return total
    
        case "sub":
            total = args[0]
            for i in range(1,len(args)):
                total -= args[i]
            return total
    
        case "mul":
            total = 1
            for num in args:
                total*=num
            return total
        
        case "div":
            total = args[0]
            for i in range(1,len(args)):
                total /= args[i]
            return total
    
        
        case "mod":
            total = args[0]
            for i in range(1,len(args)):
                total %= args[i]
            return total
        
    
def main():
    while True:
        op = input("Enter operation(sub/sum/mul/div/mod) : ").strip().lower()

        match op:
            case "sum" | "sub" | "mul" | "div" | "mod":
                break
            case _:
                print("Enter a valid operation.")
    while True:
        try:
            num = int(input("Enter the number of elements"))
            if num:
                break
        except Exception:
            print("enter a valid number")

    while True:
        try:
            arr=[]
            for i in range(num):
                value =int(input(f"Enter the number {i+1}: "))
                arr.append(value)
            if arr:
                break
        except Exception:
            print("enter the numbers properly")
        
    print(calculator(op,*arr))
main()