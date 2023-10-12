"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

import pdb
import collections


def three_sum_bf(nums):
    list_len = len(nums)
    nums.sort()

    t_sum = []
    for i in range(list_len-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1, list_len-1):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            for k in range(j+1, list_len):
                if k>j+1 and nums[k]==nums[k-1]:
                    continue
                if v_i+v_j+v_k==0:
                    v_i, v_j, v_k = nums[i], nums[j], nums[k] 
                    t_sum.append([v_i,v_j,v_k])
    return t_sum

def three_sum_tp(nums):
    """
    Two-pointer
    """
    nums.sort()

    results = []
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue

        # Init left, right
        left, right = i+1, len(nums)-1

        while left<right:
            sums = nums[i]+nums[left]+nums[right] 
            if sums<0:
                left+=1
            elif sums>0:
                right-=1
            else:
                results.append([nums[i], nums[left], nums[right]])

                # Skip duplicates
                while left<right and nums[left]==nums[left+1]:
                    left+=1
                while left<right and nums[right]==nums[right-1]:
                    right-=1

                # We have to change both points because they are the elements for 
                # creating a sum to be zero
                left+=1
                right-=1

    return results

#    for i in range(len(nums)):
#        nums[i]+

nums = [-1, 0, 1, 2, -1, -4]
print(three_sum_tp(nums))


