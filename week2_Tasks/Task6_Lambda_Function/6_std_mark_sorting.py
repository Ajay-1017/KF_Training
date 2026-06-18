
def ViewAllStudent(students_details):
    return list(map(lambda name : name , students_details.keys()))


def Sort_by_total_marks(students_details):
    return (sorted((list(map(lambda x: (x[0],sum(x[1].values())),students_details.items())))))


def sort_by_name(students_details):
    return(sorted(students_details.keys()))



def Show_passed_students(students_details):
    result = []
    for name, marks in students_details.items():
        passed_subjects = list(
            filter(
                lambda x: x[1] == "fail",
                map(lambda x: (x[0], "pass" if x[1] > 65 else "fail"),
                    marks.items())
            )
        )
        if passed_subjects:
            result.append((name, passed_subjects))
    return result

def sortBysubject(students_details,subject):
        return list((map(lambda x :(x[0],{subject:x[1][subject]}),sorted(students_details.items(), key=lambda x : x[1][subject]))))


def main():
    students_details = {
        "Vijay":  {"MAT": 78, "ENG": 85, "TAM": 90, "BIO": 88, "CS": 92},
        "Arun":  {"MAT": 78, "ENG": 85, "TAM": 90, "BIO": 88, "CS": 92},
        "Bala":  {"MAT": 65, "ENG": 70, "TAM": 80, "BIO": 75, "CS": 89},
        "Kumar": {"MAT": 92, "ENG": 95, "TAM": 87, "BIO": 91, "CS": 94},
        "Ajay": {"MAT": 55, "ENG": 60, "TAM": 58, "BIO": 72, "CS": 68}
    }

    print(ViewAllStudent(students_details))
    print(Sort_by_total_marks(students_details))
    print(sort_by_name(students_details))
    print(Show_passed_students(students_details))
    print(sortBysubject(students_details,"MAT"))
main()
























