def arm_strong(num):
    temp = num
    cnt = 0
    sum = 0

    # count the no of digits 
    while temp != 0:
        temp = temp // 10 
        cnt +=1
    
    temp = num 
    while temp != 0:
        d = temp % 10
        sum += d**cnt
        temp = temp//10
    
    if sum == num:
        return "armstrong"
    else:
        return "not a armstrong"
    
def main():
    num = int(input("enter any number : ")) # 153 , 1634
    print(arm_strong(num))
main()
