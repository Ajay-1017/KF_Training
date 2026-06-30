def remove_duplicates(lst):
    seen = set()
    ans=[]
    
    for i in lst:
        if i not in seen:
            ans.append(i)
        seen.add(i)
    return ans


def main():
    lst = [9,9,10,10,11,11,1,1,1,2,2,3,3,4,5]
    print(remove_duplicates(lst))
main()

