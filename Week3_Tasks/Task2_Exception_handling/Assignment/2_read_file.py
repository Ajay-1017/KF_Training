# 2) Read a file safely and display a friendly message if the file doesn't exist.

try:
    file = open("KF_training/Week3_Tasks/Task2_Exception_handling/Assignment/read.txt",'r')

except FileNotFoundError as e:
    print("sorry file does not exist")

else:
   print(file.read())
   file.close()


