
try:
    f = open("KF_training/Week3_Tasks/Task2_Exception_handling/Practice/corupt_file.txt",'r')

    if f.name == "KF_training/Week3_Tasks/Task2_Exception_handling/Practice/corupt_file.txt":
        raise Exception
    
except Exception:
    print("something went wrong")

try:
    f = open("KF_training/Week3_Tasks/Task2_Exception_handling/Practice/student_file.txt",'r')
    # var = bad_var

except FileNotFoundError as e:
    print(e)

except NameError as e:
    print(e)

else:
    content = f.read()
    print(content)
    f.close()

finally:
    print("Exceuting finally....")
    
