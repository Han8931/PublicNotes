"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""
import time
from datetime import timedelta
import pdb

from typing import List

#nums = [0, 4, 3, 0]

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]


def two_sum_faster(nums, target):
    """
    The index() method returns the index of the specified element in the list.
    """
    for i in range(0, len(nums)):
        complement = target-nums[i]
        if complement in nums[i+1:]:
            # Move i+1 thus, need to add i+1
            idx = nums[i+1:].index(complement)+(i+1)  
            return [i, idx]

def two_sum_dict(nums: List[int], target:int) -> List[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        nums_map[num]=i
    
    for i, num in enumerate(nums):
        if target-num in nums_map:
            return [i, nums_map[target-num]]


if __name__=="__main__":

    nums = [2, 4, 6, 15]
    target = 8

    start_t_gen = time.perf_counter()
    print(two_sum(nums, target))
    eval_t = time.perf_counter()-start_t_gen
    print(f"Total Elapsed Time: {timedelta(seconds=eval_t)}", flush=True) 

    start_t_gen = time.perf_counter()
    print(two_sum_faster(nums, target))
    eval_t = time.perf_counter()-start_t_gen
    print(f"Total Elapsed Time: {timedelta(seconds=eval_t)}", flush=True) 

    start_t_gen = time.perf_counter()
    print(two_sum_dict(nums, target))
    eval_t = time.perf_counter()-start_t_gen
    print(f"Total Elapsed Time: {timedelta(seconds=eval_t)}", flush=True) 

