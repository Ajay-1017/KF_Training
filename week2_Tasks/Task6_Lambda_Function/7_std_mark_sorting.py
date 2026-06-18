"""
--------- STUDENT MENU ---------

1. View All Students
2. Sort by Marks
3. Sort by Name
4. Show Passed Students
5. Show Failed Students
6. Show Top Scorer
7. Exit

--------------------------------
"""

def view_students(students_details):
    return list(map(lambda x : x ,students_details.keys()))


def sortByMarks(students_details,name):
    marks = list(students_details[name].items())
    marks.sort(key=lambda x : x[1])
    return marks
    
def sortByName(students_details):
    std_details= list(students_details.keys())
    std_details.sort()
    return std_details

# my approach 
# def pass_subjects(students_details,name):
#     marks=list(students_details[name].items())
#     pass_fail = list(map(lambda x : (x[0],"pass" if x[1] > 65 else ""),marks))
#     return list(filter(lambda x : x[1]=="pass",pass_fail))

def pass_subjects(students_details, name):
    return list(map(lambda x : x , filter(lambda x : x[1] > 65 , students_details[name].items())))

def fail_subjects(students_details,name):
    return list(map(lambda x : x ,filter(lambda x : x[1]<=65 ,students_details[name].items())))

def top_scorer(students_details):
    name, marks = max(
        students_details.items(),
        key=lambda x: sum(x[1].values())
    )
    return name, sum(marks.values())
    

def main():
    students_details = {
        "Vijay":  {"MAT": 78, "ENG": 85, "TAM": 90, "BIO": 88, "CS": 92},
        "Arun":  {"MAT": 78, "ENG": 85, "TAM": 90, "BIO": 88, "CS": 92},
        "Bala":  {"MAT": 65, "ENG": 70, "TAM": 80, "BIO": 75, "CS": 89},
        "Kumar": {"MAT": 92, "ENG": 95, "TAM": 87, "BIO": 91, "CS": 94},
        "Ajay": {"MAT": 55, "ENG": 60, "TAM": 58, "BIO": 72, "CS": 68}
    }
    
    print(view_students(students_details))
    print(sortByMarks(students_details,"Ajay"))
    print(sortByName(students_details))
    print(pass_subjects(students_details,"Ajay"))
    print(fail_subjects(students_details,"Ajay"))
    print(top_scorer(students_details))
main()