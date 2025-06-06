def sort(arr, n):
    for i in range(0, n):
        si = i
        for j in range(i+1, n):
            if arr[j] < arr[si]:
                temp = arr[si]
                arr[si] = arr[j]
                arr[j] = temp
        

arr = [4,9,2,3,6]
n = len(arr)
sort(arr, n)
print("List after sorting: ", arr)