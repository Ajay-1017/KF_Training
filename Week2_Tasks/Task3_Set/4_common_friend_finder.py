def main():
    persons=[]
    while True:
        try:
            n=int(input("Enter no of persons : "))
            if n>=2:
                break
        except ValueError:
            print("Enter the valid number ")
            continue
        print("Please enter atleast 2 persons")

    for i in range(n):
        print(f"person{i+1} details")
        while True:
            try:
                n = int(input("Enter the no of friends less than 6: "))
                if n>=1 and n<=5:
                    break
            except ValueError:
                print("Enter valid number")
        
        friends_set=set()
        count=0
        while count < n:
            name=input(f"Enter the friend name {count+1}: ").strip().title()
            if not name:
                print("please enter the name")
            if name in friends_set:
                print("name is already entered")
            else:
                friends_set.add(name)
                count+=1
        persons.append(friends_set)


    common = persons[0]

    for i in range(len(persons)):
        print(f"person{i+1} friends",persons[i] )
        c = common.intersection(persons[i])
    print("common friends",c)

main()