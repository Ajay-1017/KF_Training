import re
def profile():
    # Name
    while True:
        name = input("Enter the name: ").strip()
        if name:
            break
        print("Enter the valid name ")

    # Age
    while True:
        try:
            age = int(input("Enter the age: "))
            if age>=0 and age<=120:
                break
            print("enter the correct age")
        except ValueError:
            print("Enter the valid number")
    
    # Phone_number
    while True:
        phone_no = input("Enter phone number: ").strip()
        if phone_no.isdigit() and len(phone_no)==10:
            break
        print("Enter 10 didits properly")

    # Email
    while True:
        email = input("Enter the email : ")
        if re.match("^[a-z0-9]+@[a-z]+\.com$",email):
            break
        print("Enter the valid email")


    print("Name : ",name)
    print("age : ",age)
    print("phone_number : ",phone_no)
    print("Email",email)
profile()