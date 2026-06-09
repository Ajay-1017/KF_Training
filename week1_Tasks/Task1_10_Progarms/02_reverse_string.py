def rev_string(stg):
    rev = " "
    for i in stg:
        rev = i + rev
    return rev

def main():
    stg = input("enter string :")
    print(rev_string(stg))
main()

    