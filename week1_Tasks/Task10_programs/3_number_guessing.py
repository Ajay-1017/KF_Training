import random

def numberGuess(num,ran):
    if num == ran:
        return f"you got the number {ran} "
    elif num < ran:
        return f"higher"
    else:
        return f"lower"

def main():
    ran = random.randint(1,10)
    while True:
        num = int(input("Enter the number : "))
        print(numberGuess(num,ran))
        if num == ran:
            break
main()
