"""
Swap smaller elements to the left side
"""
def insertion_sort_fn(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
    return arr

arr = [1, 6, 3, 2]
arr = insertion_sort_fn(arr)
print(arr)
