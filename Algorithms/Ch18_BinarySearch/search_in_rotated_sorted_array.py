import pdb

def binary_search_rotated_array(nums, target):
    if not nums:
        return -1

    # Find the pivot
    left = 0
    right = len(nums)-1

    while left<right:
        mid = left+(right-left)//2

        if nums[mid]>nums[right]:
            left = mid+1
        else:
            right = mid

    pivot = left

    # Now we have to find the true mid point.
    # To get the true point, we need to compute how much it is pushed
    # and conduct a binary search.
    left = 0
    right = len(nums)-1
    while left<=right:
        mid = left+(right-left)//2

        # Modulo operation to deal with an index larger than the list length
        mid_true = (mid+pivot)%len(nums) 
        if nums[mid_true]<target:
            left = mid+1
        elif nums[mid_true]>target:
            right = mid-1
        else:
            return mid_true

    return -1








#nums = [4, 5, 6, 7, 0, 1, 2]
#nums = [0, 1, 2, 4, 5, 6, 7]

nums = [4, 5, 6, 7, 0, 1, 2]
print(binary_search_rotated_array(nums, 5))

