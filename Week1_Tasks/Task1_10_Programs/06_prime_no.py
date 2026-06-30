import math
def isprime(num):
    cnt = 0
    if num < 0:
        return False
    for i in range(1,int(math.sqrt(num))+1):
        if num % i == 0:
            cnt += 1
            if (num//i)!=i:
                cnt+=1
    return cnt==2

def main():
    num = int(input("enter any number : "))
    print(isprime(num))
main()


