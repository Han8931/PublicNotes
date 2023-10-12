"""
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
"""

arr = [1,4,3,2]
#arr = [6,2,6,5,1,2]

def arr_part(nums):
    nums.sort()

    sums = 0
    for i in range(0, len(nums), 2):
        sums+=nums[i]
        
    return sums

print(arr_part(arr))

def arr_part2(nums):
    return sum(sorted(nums)[::2])

print(arr_part2(arr))

    
