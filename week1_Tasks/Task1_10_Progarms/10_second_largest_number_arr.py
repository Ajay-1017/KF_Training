def second_largest(arr):
    max1=float('-inf')
    max2=float('-inf')
    for i in range(len(arr)):
        if arr[i]>max1:
            max2=max1
            max1=arr[i]
        
        elif arr[i]>max2 and arr[i]!=max1:
            max2 = arr[i]
    return max2

def main():
    arr=[]
    n = int(input("no of elements in list"))
    for i in range(n):
        d = int(input(f"enter element{i+1}: "))
        arr.append(d) 
    print(second_largest(arr))
main()
    
