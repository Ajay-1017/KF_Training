def intersection(s1,s2):
    return s1.intersection(s2)

def main():
    s1=set()
    s2=set()
    
    for i in range(2):
        print(f"person{i+1} details")
        while True:

            try:
                n = int(input("Enter the no of friends less than 6: "))
                if n>=1 and n<=5:
                    break
            except ValueError:
                print("Enter valid number")
        count=0
        while count < n:
            name=input(f"Enter the friend name {count+1}: ").strip().title()

            if i==0:
                if name in s1:
                    print("name is already entered")
                else:
                    s1.add(name)
                    count+=1
            else:
                if name in s2:
                    print("name is already entered")
                else:
                    s2.add(name)
                    count+=1
    
    print("person 1 friends :",s1)
    print("person 2 friends :",s2)
    print("\n common friends ",intersection(s1,s2))
    
main()