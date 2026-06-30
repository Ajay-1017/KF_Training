
def square_area(a):
    return a*a

def rec_area(l,b):
    return l*b

def tri_area(b,h):
    return 0.5*b*h

def get_numbers(count,message):
    while True:
        try:
            nums = list(map(int,input(message).split()))

            if len(nums)!=count:
                print(f"Enter exactly {count} number(s)")
                continue

            if any(num <= 0 for num in nums):
                print("Enter number above zero")
                continue

        except ValueError:
            print("Enter the valid number(s)")

        return nums

def main():
    ch ="yes"
    while ch=="yes":
        operations ={
            "square" : (square_area,1,"Enter the side of square :"),
            "rectangle":(rec_area,2,"Enter length and breadth : "),
            "triangle": (tri_area,2,"Enter base and height : ")
        }
        while True:
            choice = input("Enter the operations(square/rectangle/triangle)").strip().lower()
            if choice in operations:
                break
            print("\nEnter the correct operation from the list")
        
        func , count, message = operations[choice]

        nums = get_numbers(count,message)

        print(func(*nums))

        while True:
            ch = input("continue for futher calucaltion yes/no ").strip().lower()
            if ch not in ("yes","no"):
                print("Enter the correctly yes/no")
            else:
                break
            
    print("exit")
main()









            

