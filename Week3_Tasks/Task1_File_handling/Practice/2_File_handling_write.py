
# 1) 'w' -> if file does not exist create and otherwise overwrite the file

with open ("KF_training/Week3_Tasks/Task1_File_handling/Practice/write_method.txt",'w+') as file:
    file.write("HELLO")
    file.seek(0)
    file.write("W")




# 2) 'a' -> to append the content to the file instead of overwriting 

# with open ("KF_training/Week3_Tasks/Task1_File_handling/Practice/write_method.txt",'a') as file:
#     file.write("WORLD")


# 3) To copy a file to another file 

with open("KF_training/Week3_Tasks/Task1_File_handling/Practice/read_method.txt",'r') as rf:
    with open("KF_training/Week3_Tasks/Task1_File_handling/Practice/write_copy_file.txt",'w') as wf:

        for line in rf:
            wf.write(line)


# 4) To copy a image to another file (here we need to use byte mode)
with open("KF_training/Week3_Tasks/Task1_File_handling/Practice/bmw_car.png",'rb') as rf:
    with open("KF_training/Week3_Tasks/Task1_File_handling/Practice/bmw_car_copy_image.png",'wb') as wf:

        # for line in rf:
        #     wf.write(line)

        chunk_size = 4096
        read_chunk = rf.read(chunk_size)

        while len(read_chunk)>0:
            wf.write(read_chunk)
            read_chunk = rf.read(chunk_size)
