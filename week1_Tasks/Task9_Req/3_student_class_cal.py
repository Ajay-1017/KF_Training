# Overall info :
# Top Scorer
# Class Average
# Number of Passes
# Number of Fails
# Highest Subject Mark
# Lowest Subject Mark

def student_calculator(students):
    std = {}
    pas = 0
    fail = 0
    class_total = 0

    for name, marks in students.items():
        total = 0

        for mark in marks.values():
            total += mark

        avg = total / len(marks)
        class_total += avg

        if avg > 35:
            pas += 1
        else:
            fail += 1

        std[name] = {
            "total": total
        }

    class_avg = class_total / len(students)

    # Ranking
    rank_dict = {}

    for name1 in std:
        rank = 1
        for name2 in std:
            if std[name2]["total"] > std[name1]["total"]:
                rank += 1

        if rank not in rank_dict:
            rank_dict[rank] = []

        rank_dict[rank].append(name1)

    return rank_dict, class_avg, pas, fail


def subject_info(students):
    highest = -1
    lowest = 101

    high_sub = ""
    low_sub = ""

    for name, marks in students.items():
        for subject, mark in marks.items():

            if mark > highest:
                highest = mark
                high_sub = subject

            if mark < lowest:
                lowest = mark
                low_sub = subject

    return highest, high_sub, lowest, low_sub


def main():

    students = {
        "Ajay": {"Math": 78, "English": 85, "Tamil": 90, "Science": 88, "CS": 92},
        "Arun": {"Math": 78, "English": 85, "Tamil": 90, "Science": 88, "CS": 92},
        "Bala": {"Math": 65, "English": 70, "Tamil": 80, "Science": 75, "CS": 89},
        "Kumar": {"Math": 92, "English": 95, "Tamil": 87, "Science": 91, "CS": 94},
        "Vijay": {"Math": 55, "English": 60, "Tamil": 58, "Science": 72, "CS": 68}
    }

    rank_dict, class_avg, pas, fail = student_calculator(students)

    top_scorer = rank_dict[1]

    highest, high_sub, lowest, low_sub = subject_info(students)

    print("Overall Information")
    print("-------------------")

    print("Top Scorer :", end=" ")
    for name in top_scorer:
        print(name, end=" ")
    print()

    print("Class Average :", round(class_avg, 2))
    print("Number of Passes :", pas)
    print("Number of Fails :", fail)

    print("Highest Subject Mark :", highest, f"({high_sub})")
    print("Lowest Subject Mark :", lowest, f"({low_sub})")


main()