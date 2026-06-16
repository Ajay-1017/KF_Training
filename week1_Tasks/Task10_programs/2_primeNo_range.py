# There are exactly 25 prime numbers between 1 and 100.
# [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
# 1. Group by Tens
# To scan them easily, here is the list broken down into groups of 10:
# 1 to 10: 2, 3, 5, 7
# 11 to 20: 11, 13, 17, 19
# 21 to 30: 23, 29
# 31 to 40: 31, 37
# 41 to 50: 41, 43, 47
# 51 to 60: 53, 59
# 61 to 70: 61, 67
# 71 to 80: 71, 73, 79
# 81 to 90: 83, 89
# 91 to 100: 97

import math

def isprimeMyapproach(n):
    if n<=0:
        return False

    cnt=0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            cnt+=1
            if (n//i)!=i:
                cnt+=1
    return cnt==2

def isprime(n):
    if n<=0:
        return False
    
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
        
def main():
    ans1=[]
    ans2=[]
    start = int(input("Enter the start number : "))
    end = int(input("Enter the end number : "))

    for i in range(start,end+1):
        if isprime(i):
            ans1.append(i)
        if isprimeMyapproach(i):
            ans2.append(i)
    print(ans1)
    print(ans2)

main()



