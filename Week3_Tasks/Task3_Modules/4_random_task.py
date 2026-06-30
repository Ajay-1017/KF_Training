# 4) Create a password generator using the random module.

import random

def password(n):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "!@#$%^&*"

    all_characters = uppercase + lowercase + numbers + symbols
    atleast_one_char = random.choice(uppercase) + random.choice(lowercase)+random.choice(numbers)+random.choice(symbols)
    password = atleast_one_char


    for _ in range(n-4):
        password+= random.choice(all_characters)
    
    lst = list(password)
    random.shuffle(lst)
    return "".join(lst)


def main():
    n= int(input("Enter the password length : "))
    print(password(n))
main()




