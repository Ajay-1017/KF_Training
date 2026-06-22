# 1) Create a student list file, read all student names, and count the total number of students.

# write
with open("KF_training/Week3_Tasks/Task1_File_handling/Assignment/student_file.txt",'w') as wf:

    lst =["Ajay","Aravinth","Surya","Akash","Priyanka","Balu","Vijaya"]

    i=0
    for name in lst:
        wf.write(f"{i+1}. {name}\n")
        i+=1

# read
with open("KF_training/Week3_Tasks/Task1_File_handling/Assignment/student_file.txt",'r') as rf:
    cnt=0
    for line in rf:
        print(line,end="")
        cnt+=1

    print(f"total no of students is {cnt}")
    