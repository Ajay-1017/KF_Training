# 5) Raise a custom exception if marks entered are outside the range 0–100.


def main():
    print("Enter the marks of 5 subjects : ")
    marks=[]
    for i in range(5):
        while True:
            try:
                mark = int(input(f"Enter the mark of sub{i+1}: "))
                if mark < 0 or mark > 100:
                    raise ValueError("range")
            
            except ValueError as e:
                if str(e) == "range":
                    print("Enter the marks between 0 to 100")
                else:
                    print("Invalid number !!!")
            
            else:
                marks.append(mark)
                break
    print(marks)

main()
                


