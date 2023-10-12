import pdb
from datetime import timedelta
import time

def binarySearchRecursive(arr, target, low, high):
    if low>high:
        return
    
    mid = (low+high)//2
    if target==arr[mid]:
        return True
    elif target<arr[mid]:
        high = mid-1
        return binarySearchRecursive(arr, target, low, high)
    else:
        low = mid+1
        return binarySearchRecursive(arr, target, low, high)

def binarySearch(arr, target):
    length = len(arr)
    low = 0
    high = length-1

    while high>=low:
        mid = (low+high)//2

        if target==arr[mid]:
            return True
        elif target<arr[mid]:
            high = mid-1
        else:
            low = mid+1
        mid = (low+high)//2

    return False

arr = [2, 4, 5, 7, 11, 30]

start_t_gen = time.perf_counter()
print(binarySearchRecursive(arr, 6, 0, 5))
eval_t = time.perf_counter()-start_t_gen
print(f"Total Elapsed Time: {timedelta(seconds=eval_t)}", flush=True) 

start_t_gen = time.perf_counter()
print(binarySearch(arr, 30))
eval_t = time.perf_counter()-start_t_gen
print(f"Total Elapsed Time: {timedelta(seconds=eval_t)}", flush=True) 

