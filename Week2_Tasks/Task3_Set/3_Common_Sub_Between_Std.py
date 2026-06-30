def commonSub(s1, s2):
    return s1.intersection(s2)


# Practice input validation 
def main():
    valid_subjects = {"MAT", "ENG", "BIO", "TAM", "CS"}
    s1 = set()
    s2 = set()

    for i in range(2):
        print(f"\nEnter Person {i+1}'s subjects")

        while True:
            try:
                n = int(input("Enter the number of subjects (1 to 5): "))
                if 1 <= n <= 5:
                    break
                print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Enter a valid number.")

        count = 0
        while count < n:
            sub = input(f"Enter subject {count+1}: ").strip().upper()

            if sub not in valid_subjects:
                print("Invalid subject! Valid subjects are:")
                print(valid_subjects)
                continue

            if i == 0:
                if sub in s1:
                    print("Subject already entered.")
                else:
                    s1.add(sub)
                    count += 1
            else:
                if sub in s2:
                    print("Subject already entered.")
                else:
                    s2.add(sub)
                    count += 1

    common = commonSub(s1, s2)

    print("\nPerson 1 subjects:", s1)
    print("Person 2 subjects:", s2)

    if common:
        print("Common subjects:", common)
    else:
        print("No common subjects found.")

main()