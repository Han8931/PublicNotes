def bubble_sort_fn(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr

arr = [2, 4, 1, 6, 3]
print(bubble_sort_fn(arr))


