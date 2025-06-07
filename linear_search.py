def search(arr, n, s):
    for i in range(n):
        if arr[i] == s:
            return i
    return -1 #-1 is returned to indicate that the element was not found in the array.

arr = [34,12,56,23,7,10]
n = len(arr)
s = int(input("Element to be searched: "))
p = search(arr, n, s)
if p != -1:
    print(f"{s} found at {p+1} position")
else:
    print(f"{s} not found")



