def freq_count(stg):
    d={}
    for ch in stg:
        if ch in d:
            d[ch]+=1
        else:
            d[ch]=1
    return d

def main():
    stg = input("enter any string ")
    print(freq_count( stg))
main()

