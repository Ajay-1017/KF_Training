# calculates the students rank , total , average using in_built functions

def student_calculator(students):
    std = {}

    for name, marks in students.items():
        total = 0

        for mark in marks.values():
            
            total += mark
        avg = total / len(marks)

        std[name]= {"total": total,"avg": avg}

    rank_dict={}
    for name1 in std:
        rank = 1
        for name2 in std:
            if std[name2]["total"]>std[name1]["total"]:
                rank+=1
        rank_dict[rank]=name1

    return std,rank_dict
      

def main():
   
    students = {
        "Ajay":  {"Math": 45, "English": 99, "Tamil": 50, "Science": 100, "CS": 100},
        "Arun":  {"Math": 78, "English": 85, "Tamil": 90, "Science": 88,  "CS": 92},
        "Bala":  {"Math": 65, "English": 70, "Tamil": 80, "Science": 75,  "CS": 89},
        "Kumar": {"Math": 92, "English": 95, "Tamil": 87, "Science": 91,  "CS": 94},
        "Vijay": {"Math": 55, "English": 60, "Tamil": 58, "Science": 72,  "CS": 68}
        }
    
    result,rank_dict = student_calculator(students)

    for rank in range(1, len(rank_dict) + 1):

        name = rank_dict[rank]

        print(f"Rank    : {rank}")
        print(f"Name    : {name}")
        print(f"Total   : {result[name]['total']}")
        print(f"Average : {result[name]['avg']:.2f}")
        print()

main()




