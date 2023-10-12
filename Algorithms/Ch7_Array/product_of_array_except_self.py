"""
Given an integer array nums, return an array answer such that 
answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

In this problem, I have to understand the concept.
One way we can break it down is basically 
to get the product of every value before the current step 
and get the product of every value after the step.
However, we don't have to get all these numbers to save space complexity.
"""

import pdb

nums = [1,2,3,4]

def productArr(nums):
    if not nums:
        return 

    arr_len = len(nums)

    prod_ = 1
    left_p = [] # Prefix
    for i in range(arr_len):
        left_p.append(prod_)
        prod_ = prod_*nums[i]

    prod_ = 1
    for i in reversed(range(len(nums))):
    #for i in range(arr_len-1, -1, -1):
        left_p[i] = left_p[i]*prod_
        prod_ = prod_*nums[i] # Cumulative product of right elements

    return left_p

print(productArr(nums))
