"""
- Partition-exchange sort algorithm
- Divide and Conquer
- Pivot
"""

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

arr = [2, 4, 1, 6, 3]
quick_sort_fn(arr, 0, len(arr)-1)
print(arr)
