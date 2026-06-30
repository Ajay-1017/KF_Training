def isprime(num):
    cnt = 0
    if num <= 17:
        return False
    i=1
    while i*i<=num:
        if num % i == 0:
            cnt += 1
            if (num//i)!=i:
                cnt+=1
        if cnt>2:
            return False
        i+=1
    return cnt==2

def isprime1(num):
    if num <= 1:
        return False

    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1

    return True

def main():
    num = int(input("enter any number : "))
    print(isprime(num))
    print(isprime1(num))
main()


