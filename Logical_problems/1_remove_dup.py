# i/p -> [1,2,2,3,1]
# o/p -> [1,2,3]


# Method -1 

def remove_dup(lst):
    seen = set()
    ans=[]
    for num in lst:
        if num not in seen:
            ans.append(num)
        seen.add(num)
    return ans

# Method-2
def remove_dup_1(lst):
    i=0
    j=1
    while j<len(lst):
        if lst[i]!=lst[j]:
            lst[i+1] = lst[j]
            i+=1
        j+=1
    return lst[:i]

def main():
    lst = [1,2,2,3,1,1,1,1,1,1,1]
    print(remove_dup(lst))
    print(remove_dup_1(lst))
main()


            