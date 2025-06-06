def sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        #divide the arr
        l_half = arr[:mid]
        r_half = arr[mid:]

        #sorting left and right half
        sort(l_half)
        sort(r_half)

        i = j = k = 0
        while i < len(l_half) and j < len(r_half):
            if l_half[i] < r_half[j]:
                arr[k] = l_half[i]
                i = i + 1
            else:
                arr[k] = r_half[j]
                j = j + 1
            k += 1
        # for left over elements
        while i <len(l_half):
            arr[k] = l_half[i]
            i += 1
            k += 1

        while j < len(r_half):
            arr[k] = r_half[j]
            j += 1
            k += 1



arr = [28, 56, 12, 78, 91, 44, 9]
print("Before sorting: ", arr)
sort(arr)
print("\nAfter sorting: ", arr)