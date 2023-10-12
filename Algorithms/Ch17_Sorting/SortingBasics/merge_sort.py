
def merge_sort(arr):
    len_arr = len(arr)
    if len_arr<=1:
        return arr

    pivot = len_arr//2
    left_arr = merge_sort(arr[:pivot])
    right_arr = merge_sort(arr[pivot:])
    return merge(left_arr, right_arr)

def merge(left, right):
    l_cur, r_cur = 0, 0
    l_len, r_len = len(left), len(right)

    temp = []
    while l_cur<l_len and r_cur<l_len:
        if left[l_cur]<=right[r_cur]:
            temp.append(left[l_cur])
            l_cur+=1
        else:
            temp.append(right[r_cur])
            r_cur+=1

    temp.extend(left[l_cur:])
    temp.extend(right[r_cur:])
    return temp

test = [1, 6, 5, 2, 4]
print(merge_sort(test))
