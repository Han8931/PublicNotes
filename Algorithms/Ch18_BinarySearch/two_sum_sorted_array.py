import pdb

def two_sum_sorted_array_two_pointer(nums, target):
    i,j = 0, len(nums)-1

    while i<j:
        sums = nums[i]+nums[j]
        if sums<target:
            i+=1
        elif sums>target:
            j-=1
        else:
            return i+1, j+1

nums = [2, 7, 11, 15]
target = 9


def two_sum_sorted_array_bst(nums, target):
    for i, v in enumerate(nums):
        left = i+1
        right = len(nums)-1
        rem = target-v

        while left<=right:
            mid = left+(right-left)//2

            if nums[mid]<rem:
                left= mid+1
            elif nums[mid]>rem:
                right = mid-1
            else:
                return i+1, mid+1

import bisect

def two_sum_sorted_array_bisect(nums, target):
    for i, v in enumerate(nums):
        rem = target-v
        num_list = nums[i+1:]
        index = bisect.bisect_left(num_list, rem)
        if index<len(num_list) and nums[i+1+index]==rem: 
            return index+1, index+i+2

print(two_sum_sorted_array_two_pointer(nums, target))
print(two_sum_sorted_array_bst(nums, target))
print(two_sum_sorted_array_bisect(nums, target))
