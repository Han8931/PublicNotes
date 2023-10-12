import pdb

# Simple implementation
def quick_sort_fn(arr, lo, hi):

    def partition(lo, hi):
        pivot = arr[hi] # Set the right end elements as a pivot first
        left = lo
        for right in range(lo, hi):
            if arr[right]<pivot:
                # Swap if the right pointer's element is smaller than the pivot
                arr[right], arr[left] = arr[left], arr[right]
                left+=1

        # Sawp once we put all small elements to the left side.
        arr[left], arr[hi] = arr[hi], arr[left]
        return left

    if lo<hi:
        pivot = partition(lo, hi)
        quick_sort_fn(arr, lo, pivot-1)
        quick_sort_fn(arr, pivot+1, hi)


def quickSort(arr, start, end):
    if start>=end:
        return 

    pivot = start
    left = start+1
    right = end

    while left<=right:
        while left<=end and arr[left]<=arr[pivot]:
            # Left marker stops if it is larger than the pivot
            left+=1
        while right>start and arr[right]>=arr[pivot]:
            # Right marker stops if it is smaller than the pivot
            right-=1

        if left>right:
            # The left marker is still smaller than the pivot
            # THe right marker is still larger than the pivot
            # ex) [8, 6, 9], pivot=8, left=6, right=9
            # ex) [8, 6, 9], pivot=8, right=6, left=9
            # Swap, [6, 8, 9]
            arr[pivot],arr[right] = arr[right], arr[pivot]
        else:
            # Left marker is bigger than the pivot and right marker is smaller than the pivot.
            # So swap them.
            arr[left],arr[right] = arr[right], arr[left]


    quickSort(arr, start, right-1)
    quickSort(arr, right+1, end)


arr = [10, 5, 51, 18, 4, 2, 4, 3]
print(arr)
quickSort(arr, 0, len(arr)-1)
print(arr)


