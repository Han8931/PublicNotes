import pdb

def merge_sort(arr):
    length = len(arr)
    if length<=1:
        return arr
    pivot = length//2

    left_arr = merge_sort(arr[:pivot])
    right_arr = merge_sort(arr[pivot:])
    return merge(left_arr, right_arr)

def merge(left_arr, right_arr):
    l_cur = 0
    r_cur = 0
    l_len = len(left_arr)
    r_len = len(right_arr)

    temp = []
    while l_cur<l_len and r_cur<r_len:
        if left_arr[l_cur]<=right_arr[r_cur]:
            temp.append(left_arr[l_cur])
            l_cur+=1
        else:
            temp.append(right_arr[r_cur])
            r_cur+=1
    temp.extend(left_arr[l_cur:])
    temp.extend(right_arr[r_cur:])
    return temp

test = [1, 6, 5, 2, 4]

print(merge_sort(test))

