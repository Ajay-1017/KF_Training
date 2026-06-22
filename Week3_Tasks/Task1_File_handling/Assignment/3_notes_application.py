# 3) Create a notes application with options to add and view notes.

def main():
    while True: 
        choice = input("add/view/exit : ")
        if choice == "exit":
            break
        file_name = input("Enter the file_name : ")

        match choice:
            case "add":
                with open(f"KF_training/Week3_Tasks/Task1_File_handling/Assignment/{file_name}.txt", 'a') as f:
                    print("Enter your notes : ")
                    while True:
                        line = input()
                        if line == "":
                            print("Your notes as been saved to the file successfully")
                            break
                        f.write(f"{line}\n")

            
            case "view":
                with open(f"KF_training/Week3_Tasks/Task1_File_handling/Assignment/{file_name}.txt", 'r') as f:
                    for line in f:
                        print(line,end="")
            
  
main()
