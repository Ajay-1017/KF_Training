# 2) Create a marks file and calculate the highest mark, lowest mark, total, and average.

# write
with open("KF_training/Week3_Tasks/Task1_File_handling/Assignment/mark_file.txt",'w') as wf:

    marks = [100,85,45,65,95]

    for mark in marks:
        wf.write(f"{mark}\n")

        

# Read
# Method - 1  (Normal)
with open("KF_training/Week3_Tasks/Task1_File_handling/Assignment/mark_file.txt",'r') as rf:

    marks = rf.readlines()
    max_mark = float('-inf')
    min_mark = float('inf')
    total=0
    cnt=0
    for mark in marks:
        cnt+=1
        mark = int(mark)
        total+=mark
        if mark > max_mark :
            max_mark = mark
        if mark < min_mark:
            min_mark = mark

    avg_mark = total / cnt
    print(f"total : {total}")
    print(f"Highest_mark : {max_mark}")
    print(f"Lowest_mark : {min_mark}")
    print(f"average_mark : {avg_mark}\n")

# Method - 2 (using list comprehension )
with open("KF_training/Week3_Tasks/Task1_File_handling/Assignment/mark_file.txt",'r') as rf:
    marks = [int(line) for line in rf]

print("total :", sum(marks))
print("highest Mark :", max(marks))
print("lowest Mark :", min(marks))
print("average Mark :", sum(marks) / len(marks))



               





        