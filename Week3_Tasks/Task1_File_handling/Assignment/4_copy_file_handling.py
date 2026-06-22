# 4) Copy the contents of one file into another file.

with open("KF_training/Week3_Tasks/Task1_File_handling/Assignment/student_file.txt",'r') as rf:
    with open("KF_training/Week3_Tasks/Task1_File_handling/Assignment/copy_student_file.txt",'w') as wf:

        # contents = rf.readlines()
        # for con in contents:
        #     wf.write(con)

        # for line in rf:
        #     wf.write("*"+line)

        chunk = 5
        contents = rf.read(chunk)

        while len(contents) > 0:
            wf.write(f"{contents}...")
            contents = rf.read(chunk)


