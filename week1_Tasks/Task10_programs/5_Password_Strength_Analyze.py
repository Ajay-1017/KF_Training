# # Method - 1

import re
def password_strength_analyzer1(stg):
    cnt=0
    if len(stg)>=8:
        cnt+=1
    if re.search("[a-z]",stg):
        cnt+=1
    if re.search("[A-Z]",stg):
        cnt+=1
    if re.search("[0-9]",stg):
        cnt+=1
    if re.search("[@#$%&*!]",stg):
        cnt+=1
    print(cnt)
    if cnt>=5:
        return "strong"
    
    elif cnt>=3:
        return "medium"

    else:
        return "weak"
    
def main():
    while True:
        stg = input("enter password")
        if stg=="exit":
            break
        print(password_strength_analyzer1(stg))
main()
    

# # Method - 2
import re

def password_strength_analyzer2(stg):
    cnt=0
    patterns = ["[a-z]","[A-Z]","[0-9]","[@#$%&*!]"]
    if len(stg)>=8:
        cnt+=1
    for pattern in patterns:
        if re.search(pattern,stg):
            cnt+=1
    print(cnt)
    if cnt>=5:
        return "strong"

    elif cnt>=3:
        return "medium"

    else:
        return "weak"
    
def main():
    while True:
        stg = input("enter password")
        if stg=="exit":
            break
        print(password_strength_analyzer2(stg))
main()    

# Method - 3 (pythonic way)

import re
def password_strength_analyzer3(stg):
    cnt=0
    patterns = ["[a-z]","[A-Z]","[0-9]","[@#$%&*!]"]

    cnt = (len(stg) >= 8) + sum( bool(re.search(pattern, stg)) for pattern in patterns )
    
    if cnt>=5:
        return f"strong"

    elif cnt>=3:
        return f"medium"

    else:
        return f"weak"

def main():
    while True:
        stg = input("enter password")
        if stg=="exit":
            break
        print(password_strength_analyzer3(stg))
main()    
