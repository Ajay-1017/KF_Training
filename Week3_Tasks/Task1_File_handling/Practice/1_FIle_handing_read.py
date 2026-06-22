
# 1) File objects

# write in a file (This will over write if file already exist or creates a new file)

f = open("KF_training/Week3_Tasks/Task1_File_handling/Practice/write_read_sample.txt",'w')
f.write("hello")
f.close()



# 2) Context Manager (with keyWord)
# 'r' -> to read a file

with open("KF_training/Week3_Tasks/Task1_File_handling/Practice/write_read_sample.txt",'r') as file:
    print(file.read())



# 3) read  methods -> read() , readline() , readlines() 


# # readline()
# with open("KF_training/Week3_Tasks/Task1_File_handling/Practice/read_method.txt",'r') as file:
#     con = file.readline()
#     print('\n'+ con) 


# # readlines() -> returns list 
# with open("KF_training/Week3_Tasks/Task1_File_handling/Practice/read_method.txt",'r') as file:   
#     contents = file.readlines()
#     print(contents,"\n")


# # iterating the file using for loop
# with open("KF_training/Week3_Tasks/Task1_File_handling/Practice/read_method.txt",'r') as file:
#     for line in file:
#         print(line,end="")


# # read()
# with open("KF_training/Week3_Tasks/Task1_File_handling/Practice/read_method.txt",'r') as file:
#     contents = file.read(100) # reads 1st 100 characters
#     print(contents,end='')

#     contents = file.read(100) # reads next 100 charcters 
#     print(contents,end='')

#     contents = file.read(100) # reads next 100 charcters 
#     print(contents,end='')

#     contents = file.read(100) # reads next 100 charcters if not exits reads nothing 
#     print(contents)   


#     print(f"{file.tell()} current position of the file \n")


# # 4) tell() 
# with open("KF_training/Week3_Tasks/Task1_File_handling/Practice/read_method.txt",'r') as file:
#     size_to_read = 10

#     contents = file.read(size_to_read) 

#     while len(contents)>0:
#         print(contents,end="*")
#         contents = file.read(size_to_read) 

#     print(f"\n{file.tell()} current position of the file ")

    
# 5) seek() -> file object method used to reposition the file pointer (cursor) to a 
#              specified byte offset within a file, allowing random access to file contents.

with open("KF_training/Week3_Tasks/Task1_File_handling/Practice/read_method.txt",'r') as file:

    contents = file.read(10) # reads 1st 100 characters
    print(contents,end='')

    file.seek(0) # start from the beginning of the file 

    contents = file.read(10) # reads next 100 charcters 
    print(contents)







