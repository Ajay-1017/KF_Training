

import sys

if len(sys.argv)<2:
    print("No command provided.")
    print()
    print("Type:")
    print("python student.py help")

else:
    args=sys.argv
    print(args)
    choice  = sys.argv[1]
    match choice:
        case "add":
            if len(sys.argv)==5:
                try:
                    int(sys.argv[3])
                    print("Name :", sys.argv[2])
                    print("Age  :", sys.argv[3])
                    print("City :", sys.argv[4])
                    print("student add sucessfully")
                except ValueError:
                    print('Age must be an integer.')

            else:
               print("Usage:")
               print("python student.py add <name> <age> <city>")
            
        case "show":
            print(f"showing the details of {sys.argv[2]}")

        case 'delete':
            print((f"delete the details of {sys.argv[2]}"))

        case 'update':
            print(f'{sys.argv[2]} city updated to {sys.argv[3]}')    

        case 'help':
            print("Usage:")
            print("python student.py add <name> <age> <city>")
            print("python student.py show <name>")
            print("python student.py delete <name>")
            print("python student.py update <name> <new_city>")

        case _:
            print("unknown command")
