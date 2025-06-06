def sort(arr, n):
    for i in range(0, n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
        if not swapped:
            break


arr = [4,9,2,3,6]
n = len(arr)
sort(arr, n)
print("list after sorting: ",arr)

#i have used a flag variable to optimize the code