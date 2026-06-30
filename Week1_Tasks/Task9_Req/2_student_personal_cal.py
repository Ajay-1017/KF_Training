# calculates the each student subject grades ,pass/fail,total,average

def student_cal(std_marks):

    student_details=[]

    grades={}
    total_avg={}
    pass_fail={}


    total = 0 
    for sub,mark in std_marks.items():
        # total marks
        total+=mark
        
        #pass/fail
        if mark <= 35:
            pass_fail[sub]="fail"
        if mark>35:
            pass_fail[sub]="pass"
  
        # grades
        if mark >= 90:
            grades[sub]="A"
        elif mark >= 80 and mark < 90:
            grades[sub]="B"
        elif mark >= 70 and mark < 80:
            grades[sub]="c"
        elif mark >= 60 and mark < 70:
            grades[sub]="D"
        elif mark < 60:
            grades[sub]="F"


    # average
    avg = total / len(std_marks)

    total_avg["total"]=total
    total_avg["average"]=avg
    
    student_details.append(grades)
    student_details.append(pass_fail)
    student_details.append(total_avg)
    
    return student_details

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
    student_details= student_cal(std_marks)

    headings = ["---------grade---------",
                "---------pass---------",
                "---------results---------"]

    for i in range(len(student_details)):
        print(headings[i])
        for key, value in student_details[i].items():
            print(f"{key} : {value}")
main()
        
    
    



    

