# 3) calculates the each student subject pass/fail and total , average

def student_cal(std_marks):

    std_pass_fail={}
    std_total_avg={}
    for sub,mark in std_marks.items():
        if mark < 35:
            std_pass_fail[sub]="Fail"
        else:
            std_pass_fail[sub]="Pass"
    total = 0
    for sub,mark in std_marks.items():
        total+=mark
    avg = total / len(std_marks)
    
    std_total_avg["results"]={
            "total":total,
            "average":avg
        }
    return std_pass_fail , std_total_avg
    
    


def main():
    std_marks={}
    sub =["mat","sci","cs","tam","eng"]
    for i in range(len(sub)):
        while True:
            mark = int(input(f"enter the marks of {sub[i]} :"))
            if mark >=0 and mark<=100:
                std_marks[sub[i]]=mark
                break
            print ("enter the mark within 0 to 100 ")
    std_pass_fail , std_total_avg  = student_cal(std_marks)

    print("\npass/fail : ")
    for sub,markk in std_pass_fail.items():
        print(f"{sub} : {markk} ")

    print("\ntotal & avg : ")
    for key, mark in std_total_avg["results"].items():
            print(f"{key}: {mark}")

main()
        
    
    



    

