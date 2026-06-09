def remove_dup(arr): # arr [1,1,2,3,4,4,4,4,5]
    i=0
    j=1
    while j<len(arr):
        if arr[i]!=arr[j]:
            arr[i+1]=arr[j]
            i+=1
        j+=1
    return arr[0:i+1]
def main():
    arr=[]
    n = int(input("no of elements in list"))
    for i in range(n):
        d = int(input(f"enter element{i+1}: "))
        arr.append(d) 
    print(remove_dup(arr))
main()