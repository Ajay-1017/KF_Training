def menu():
    print("\n===== STUDENT MARKS MANAGEMENT SYSTEM =====")
    print("1. Add Marks")
    print("2. Display Marks")
    print("3. Highest Mark")
    print("4. Lowest Mark")
    print("5. Average Mark")
    print("6. Remove Duplicates")
    print("7. Sort Marks")
    print("8. remove mark")
    print("9. Exit")


def highest(marks):
    high = float('-inf')
    for i in range(len(marks)):
        if marks[i] > high:
            high = marks[i]
    return high

def lowest(marks):
    low = float('inf')
    for i in range(len(marks)):
        if marks[i] < low:
            low = marks[i]
    return low

def average(marks):
    total = 0
    for i in range(len(marks)):
        total+=marks[i]
    avg = total / len(marks)
    return avg

def remove_duplicates(marks):
    marks.sort()
    i=0
    j=0
    while j<len(marks):
        if marks[i]!=marks[j]:
            marks[i+1]=marks[j]
            i+=1
        j+=1
    return marks[0:i+1]

# def remove_duplicates(marks):
#     seen=set()
#     ans=[]
#     for mark in marks:
#         if mark not in seen:
#             ans.append(mark)
#         seen.add(mark)
#     marks[:]=ans
#     return marks

def sort_marks(marks):
    marks.sort()

def remove_mark(marks,value):
    v=marks.index(value)
    marks.pop(v)


def user(n,marks):
    for i in range(n):
        while True:
            try:
                mark = int(input(f"Enter mark out of 100 of subject {i+1} : "))
                if mark>=0 and mark<=100:
                    break
                else:
                    print("Enter the number from 0 to 100")
            except ValueError:
                print("Enter integer",end=" & ") 
            
        marks.append(mark)
    return marks

def main():
    n=int(input("Enter the no of subjects "))
    marks=[]
    marks=user(n,marks)

    while True:
        menu()
        try:
            choice = int(input("Enter the choice from above menu"))
        except ValueError:
            print("Enter an integer")
            continue
        
        match choice:
            
            case 1:
                n=int(input("Enter the no of subjects "))
                marks=user(n,marks)
                print("\nMarks added : ",marks)
            
            case 2:
                print("\nMarks : ", marks)
            
            case 3:
                if marks:
                    print("\nhighest mark : ",highest(marks))
                else:
                    print("no marks avaiable")
            
            case 4:
                if marks:
                    print("\nlowest mark : ",lowest(marks))
                else:
                    print("no marks avaiable")

            case 5:
                if marks:
                    print("\naverage mark : ",average(marks))
                else:
                    print("no marks avaiable")

            
            case 6:
                if marks:
                    print("\nremoved duplicates marks : ",remove_duplicates(marks))
                else:
                    print("no marks avaiable")

            case 7:
                sort_marks(marks)
                print("\nsorted marks : ",marks)
            
            case 8:
                value=int(input("Enter the value should be removed "))
                if value in marks:
                    remove_mark(marks,value)
                    print("\nvalue removed marks : ",marks)
                else:
                    print("value not in marks")

            case 9:
                print("-----------EXIT----------")
                break

            case _:
                print("Enter the correct number from menu ")

main()

        


