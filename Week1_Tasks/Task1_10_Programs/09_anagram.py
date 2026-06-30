def anagram(stg1,stg2):
    if len(stg1)!=len(stg2):
        return False
    d={}
    for ch in stg1:
        if ch in d:
            d[ch]+=1
        else:
            d[ch]=1
    for ch in stg2:
        if ch not in d or d[ch]==0:
            return False
        d[ch]-=1
    return True

def main():
    stg1 = input("enter input1 : ")
    stg2 = input("enter input2 : ")
    print(anagram(stg1,stg2))
main()



