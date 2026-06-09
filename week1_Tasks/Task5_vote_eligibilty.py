def vote_eligibility(age):
    if age >= 18:
        return "you are eligible to vote"
    else:
        return "you are not eligible to vote"

def main():
    while True:
        try:
            age = int(input("Enter you age : "))
            if age >=0 and age<=120:
                break
            print("Enter the correct age")
        except ValueError:
            print("Enter the age in number")
    print(vote_eligibility(age))
main()



