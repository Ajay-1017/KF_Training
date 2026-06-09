# 1) calculates the students rank , total , average without using in_built functions

def student_calculator(students):
    std={}
    
    for name in students:
        sub_marks = students[name]
        total = 0
        for mark in sub_marks:
            total += sub_marks[mark]
        
        avg=total/len(sub_marks)
        std[name]={
            "total":total,
            "avg":avg
        }

    rank_dict={}
    for name1 in std:
        rank=1
        for name2 in std:
            if std[name2]["total"]>std[name1]["total"]:
                rank+=1
        rank_dict[rank]=name1

    return std , rank_dict

def main():
   
   students = {
    "Ajay":  {"Math": 45, "English": 99, "Tamil": 50, "Science": 100, "CS": 100},
    "Arun":  {"Math": 78, "English": 85, "Tamil": 90, "Science": 88,  "CS": 92},
    "Bala":  {"Math": 65, "English": 70, "Tamil": 80, "Science": 75,  "CS": 89},
    "Kumar": {"Math": 92, "English": 95, "Tamil": 87, "Science": 91,  "CS": 94},
    "Vijay": {"Math": 55, "English": 60, "Tamil": 58, "Science": 72,  "CS": 68}
    }
   
   std , rank_dict = student_calculator(students)

   for i in range(1,len(std)+1):
       name = rank_dict[i]
       print(f"rank : {i}")
       print(f"name : {name}")
       print(f"total : {std[name]["total"]}")
       print(f"avg : {std[name]["avg"]}")
       print("")
 
main()
