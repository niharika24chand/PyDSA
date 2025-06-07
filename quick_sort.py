def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for k in range(low, high):
        if pivot > arr[k]:
            i += 1
            temp = arr[i]
            arr[i] = arr[k]
            arr[k] = temp
    i += 1
    temp = arr[i]
    arr[i] = arr[high]
    arr[high] = temp
    return i


def sort(arr, low, high):
    if low < high:
        piv_index = partition(arr, low, high)
        sort(arr, low, piv_index - 1)
        sort(arr, piv_index + 1, high)


arr = [4,9,2,3,6]
n = len(arr)
sort(arr, 0, n-1)
print("List after sorting: ",arr)
