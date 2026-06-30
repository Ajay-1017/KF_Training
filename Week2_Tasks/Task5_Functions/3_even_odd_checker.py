def even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
    
def main():
    n=int(input("\nEnter any number: "))
    print(even_odd(n))
main()    