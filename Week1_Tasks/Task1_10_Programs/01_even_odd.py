def even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
def main():
    num = int(input("Enter any number"))
    print(even_odd(num))
main() 