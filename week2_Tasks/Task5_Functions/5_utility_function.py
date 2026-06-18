
def even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"

def isprime(num):
    if num <= 1:
        return False

    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1

    return True

def add(a,b): 
    return a+b

def sub(a,b): 
    return a-b



def main():
    while True:
        choice = int(input(
"""

1. Number Utilities
2. Mathematical Utilities
3. Exit

Enter your choice (1-3): 
                    
"""
        ))
        match choice:
            case 1:
                sub_choice = int(input(
"""
                            
1. even_odd
2. prime_number

Enter your choice 

"""
                ))

                match sub_choice:
                    case 1:
                        n=int(input("\nEnter any number: "))
                        print(even_odd(n))
                    
                    case 2:
                        num = int(input("enter any number : "))
                        print(isprime(num))

            case 2:
                sub_choice = int(input(
"""
                
1. add
2. sub

Enter your choice 

"""
                )) 

                match sub_choice:
                    case 1: 
                        a, b = map(int,input("Enter two numbers: ").split())
                        print(add(a,b))
                    
                    case 2:
                        a, b = map(int,input("Enter two numbers: ").split())
                        print(sub(a,b))
            
            case 3:
                break
  
main()    
                    




