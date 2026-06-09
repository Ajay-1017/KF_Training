# # 1) simple calculator with two numbers only 
# def calculator(operation,a,b):
#     if operation == "sum":
#         return a+b
#     elif operation == "sub":
#         return a-b
#     elif operation =="mul":
#         return a*b
#     elif operation =="div":
#         return a/b
#     elif operation =="mod":
#         return a%b
    
# def main():
#     while True:
#         operation = input("Enter operation properly sub/sum/mul/div/mod : ")
#         op = operation.strip().lower()
#         if op == "sub" or op=="sum" or op=="mul" or op =="div" or op =="mod":
#             break
#         print("enter operation properly from the list sub/sum/mul/div/mod ")

#     a = int(input("enter number 1 : "))
#     b = int(input("enter number 2: "))
#     print(calculator(op,a,b))
# main()


# # 2) calculator with multiple numbers with if else
# def calculator(operation,*args):
#     if operation == "sum":
#         total = 0
#         for num in args:
#             total+=num
#         return total
    
#     elif operation == "sub":
#         total = args[0]
#         for i in range(1,len(args)):
#             total -= args[i]
#         return total
    
#     elif operation =="mul":
#         total = 1
#         for num in args:
#             total*=num
#         return total
    
#     elif operation =="div":
#         total = args[0]
#         for i in range(1,len(args)):
#             total /= args[i]
#         return total
    
        
#     elif operation =="mod":
#         total = args[0]
#         for i in range(1,len(args)):
#             total %= args[i]
#         return total
        
    
# def main():
#     while True:
#         operation = input("Enter operation properly sub/sum/mul/div/mod : ")
#         op = operation.strip().lower()
#         if op == "sub" or op=="sum" or op=="mul" or op =="div" or op =="mod":
#             break
#         print("enter operation properly from the list sub/sum/mul/div/mod ")

#     num = int(input("Enter the number of elements"))
#     arr=[]
#     for i in range(num):
#         value =int(input(f"Enter the number {i+1}: "))
#         arr.append(value)
#     print(calculator(op,*arr))
# main()


# # 3) calculator with multiple numbers with match case

# def calculator(operation,*args):

#     match operation:
#         case "sum":
#             total = 0
#             for num in args:
#                 total+=num
#             return total
    
#         case "sub":
#             total = args[0]
#             for i in range(1,len(args)):
#                 total -= args[i]
#             return total
    
#         case "mul":
#             total = 1
#             for num in args:
#                 total*=num
#             return total
        
#         case "div":
#             total = args[0]
#             for i in range(1,len(args)):
#                 total /= args[i]
#             return total
    
        
#         case "mod":
#             total = args[0]
#             for i in range(1,len(args)):
#                 total %= args[i]
#             return total
        
    
# def main():
#     while True:
#         op = input("Enter operation(sub/sum/mul/div/mod) : ").strip().lower()

#         match op:
#             case "sum" | "sub" | "mul" | "div" | "mod":
#                 break
#             case _:
#                 print("Enter a valid operation.")
#     while True:
#         try:
#             num = int(input("Enter the number of elements"))
#             if num:
#                 break
#         except Exception:
#             print("enter a valid number")

#     while True:
#         try:
#             arr=[]
#             for i in range(num):
#                 value =int(input(f"Enter the number {i+1}: "))
#                 arr.append(value)
#             if arr:
#                 break
#         except Exception:
#             print("enter the numbers properly")
        
#     print(calculator(op,*arr))
# main()


def calculator(expression):
    arr = expression.split()

    result = float(arr[0])

    for i in range(1, len(arr), 2):
        op = arr[i]
        num = float(arr[i + 1])

        match op:
            case "+":
                result += num
            case "-":
                result -= num
            case "*":
                result *= num
            case "/":
                if num == 0:
                    return "Division by zero is not allowed"
                result /= num
            case _:
                return "Invalid operator"

    return result


def main():
    while True:
        expression = input("Enter expression (example: 10 + 20 - 5 * 2): ")
        arr = expression.split()

        valid = True

        # Check numbers
        for i in range(0, len(arr), 2):
            try:
                float(arr[i])
            except:
                valid = False
                break

        # Check operators
        if valid:
            for i in range(1, len(arr), 2):
                if arr[i] not in ('+', '-', '*', '/'):
                    valid = False
                    break

        if not valid:
            print("Enter the expression properly")
            continue

        break

    print("Answer =", calculator(expression))


main()
        
