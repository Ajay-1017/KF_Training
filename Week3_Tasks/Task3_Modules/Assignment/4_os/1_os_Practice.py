import os
from datetime import datetime

# 1) dir(os) -> shows all attributes and methods of os 
# print(dir(os)) 



# 2) To get the current directory path
# print(os.getcwd())



# 3) To change directory path
# os.chdir("/home/ajay.b@knackforge.com/Desktop/python/KF_training/Week3_Tasks/Task3_Modules")
# print(os.getcwd())



# 4) To list the folders and files inside directory
# print(os.listdir())



# ====================================================================

# 5)To create a directory
# os.chdir("/home/ajay.b@knackforge.com/Desktop")
# os.mkdir("tasks")
# print(os.listdir())
 
# 5a) To create a directory with sub folders
# os.makedirs("tasks/sub_tasks")

# ====================================================================

# 6) To remove specific directory only it is empty 
# os.rmdir("tasks/sub_tasks")
# print(os.listdir())

# 6a) To remove directory with sub folders only it is empties
# os.removedirs("tasks/sub_tasks")
# print(os.listdir())

# ====================================================================



# 7) To rename files or folders
# os.rename("tasks","os_demo")
# print(os.listdir())



# 8) To see the info of the folder
# print(os.stat("os_demo"))

# last_modfied_time = os.stat("os_demo").st_mtime
# print(datetime.fromtimestamp(last_modfied_time))



# 9) walk() -> To traverse all directories, subdirectories, and files in a directory tree

# for  dir_path, dir_names , file_names in os.walk("/home/ajay.b@knackforge.com/Desktop/python/KF_training/Week3_Tasks"):
#     print("dir_path:",dir_path)
#     print("dir_names",dir_names)
#     print("file names",file_names)
#     print()



# 10) environ-> Stores all environment variables in a dictionary-like object.

# print(os.environ)

# OUTPUT (SHORTENED)
# {
#     'HOME': '/home/ajay',
#     'USER': 'ajay',
#     'PATH': '/usr/bin:/bin:/usr/local/bin',
#     ...
# }

# print(os.environ.get('HOME')) # gives the home directory 



# 11) os.path.join(takes 2 arguments) -> joins path 

# file_path = os.path.join(os.environ.get('HOME'),"Desktop/python/text.txt")

# with open(file_path,'w') as f:
#     f.write("HelloWorld!!!")




