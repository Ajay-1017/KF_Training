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



def main():
    lst = [1,2,2,3,1]
    print(remove_dup(lst))
main()


        