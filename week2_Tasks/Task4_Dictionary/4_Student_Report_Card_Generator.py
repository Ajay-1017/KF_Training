# ------ REPORT CARD ------

# Name : John

# Math       : 90
# Science    : 85
# English    : 95

# Total      : 270
# Average    : 90.0
# Highest    : English
# Lowest     : Science
# Result     : PASS

# -------------------------



def report_card(student_details):
    std_details ={}
    results={}

    for name , details in student_details.items():
        total=0
        max_mark=float('-inf')
        min_mark=float('inf')
        for sub , mark in details.items():

            total += mark

            if mark > max_mark:
                max_mark=mark
                max_sub = sub
            if mark<min_mark:
                min_mark=mark
                min_sub = sub


        avg =total/len(student_details[name])
        if avg > 45:
            result = "pass"
        else:
            result = "fail"

        std_details[name]={
            "sub":details,
            "total" : total,
            "average": avg,
            "max_sub_mark": f"{max_sub} = {max_mark}",
            "min_sub_mark": f"{min_sub} = {min_mark}",
            "result" : result,
        }
        
    return std_details


    
        


    
    



def main():
    students_details = {
        "Ajay":  {"MAT": 78, "ENG": 85, "TAM": 90, "BIO": 88, "CS": 92},
        "Arun":  {"MAT": 78, "ENG": 85, "TAM": 90, "BIO": 88, "CS": 92},
        "Bala":  {"MAT": 65, "ENG": 70, "TAM": 80, "BIO": 75, "CS": 89},
        "Kumar": {"MAT": 92, "ENG": 95, "TAM": 87, "BIO": 91, "CS": 94},
        "Vijay": {"MAT": 55, "ENG": 60, "TAM": 58, "BIO": 72, "CS": 68}
    }
    # students_details = {}
    # valid_subjects = {"MAT", "ENG", "TAM", "BIO", "CS"}

    # while True:
    #     try:
    #         n = int(input("Enter the persons (upto 4) : "))
    #         if n>=1 and n<=4:
    #             break
    #         if n==0:
    #             print("Enter atleast one person")
    #     except ValueError:
    #         print("Enter the valid number")

    # for i in range(n):
    #     seen=set()
    #     subjects={}
    #     name = input(f"Enter the name of student {i+1} : ")
    #     while True:
    #         try:
    #             n = int(input("Enter the no of subjects (not more than 5 subjects) : "))
    #             if n>=1 and n<=5:
    #                 break
    #             if n==0:
    #                 print("Enter atleast one subject")
    #         except ValueError:
    #             print("Enter the valid number")

    #     for j in range(n):
    #         while True:
    #             sub = input(f"Enter the subject name {j+1} from the list ['MAT','ENG','TAM','BIO','CS'] : ")

    #             if sub.upper() not in valid_subjects:
    #                 print('invalid subject !')
    #                 print(f"select subjects from the list  ")
    #                 continue

    #             if sub.upper() in seen:
    #                 print("already entered Enter another subject")
    #                 continue

    #             else:
    #                 seen.add(sub.upper())
    #                 break
        
    #         while True:
    #             try:
    #                 mark = int(input(f"Enter the mark(out of 100) of {sub.upper()} : "))
    #                 if mark>=0 and mark<=100:
    #                     subjects.update({sub.upper() : mark})
    #                     break
    #                 else:
    #                     print("please enter the mark in range (0 - 100)")
    #             except ValueError:
    #                 print("Enter the valid number")
    #     students_details.update({ name : subjects})

    
    std_details = report_card(students_details)

    for name , details in std_details.items():
        print("\n------ REPORT CARD ------")
        print("\nName:",name)
        print()
        for key , value in details.items():
            print(f"{key} : {value}")
    print("\n-------------------------\n")



main()


    
