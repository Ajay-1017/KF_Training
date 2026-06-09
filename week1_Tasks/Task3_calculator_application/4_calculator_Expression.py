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
        
