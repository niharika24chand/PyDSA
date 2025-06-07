def search(arr, start, end, s):
    while( start <= end):
        mid = (start + end)//2
        if s == arr[mid]:
            return mid
        elif s > arr[mid]:
            start = mid + 1
        else:
            end = mid -1
    return -1       

arr = [-1, 0, 3, 4, 5, 9, 12, 19]
s = int(input("Element to be searched: "))
n = len(arr) 
p = search(arr, 0 , n-1, s)
if p != -1:
    print(f"{s} found at {p+1} position")
else:
    print(f"{s} not found")


