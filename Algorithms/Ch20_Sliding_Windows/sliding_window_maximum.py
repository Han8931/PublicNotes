

def sliding_window_max_slow(nums, k):
    if not nums:
        return 

    result = []
    for i in range(len(nums)-k+1):
        result.append(max(nums[i:i+k]))
    return result


#def sliding_window_max_fast(nums, k):
#    result = []
#    max_v = max(nums[:k])
#    for i in range(len(nums)-k+1):
#        result.append(max(nums[i:i+k]))
#    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(sliding_window_max_slow(nums, k))
