# Build a file explorer that lists all files in a directory using the os module.

import os

def file_explorer(file_path):
    for item in os.listdir(file_path):
        full_path = os.path.join(file_path, item)

        if os.path.isfile(full_path):
            print(item)
            
def main():
    file_explorer("/home/ajay.b@knackforge.com/Desktop/python/KF_training/week1_Tasks/Task1_10_Progarms")
main()


