def binary_search_rec(nums, target):
    def binary_split(left, right):
        if left<=right:
            mid = left+(right-left)//2
            #mid = (left+right)//2 # This part can cause an overflow issue


            if nums[mid]==target:
                return True
            elif nums[mid]<target:
                left = mid+1
                return binary_split(left, right)
            else:
                right = mid-1
                return binary_split(left, right)
        else:
            return False

    return binary_split(0, len(nums)-1)

nums = [1, 3, 4, 6]
print(binary_search_rec(nums, 5))

def binary_search_iter(nums, target):
    left, right = 0, len(nums)-1

    while left<=right:
        mid = left+(right-left)//2
        #mid = (left+right)//2 # This part can cause an overflow issue

        if nums[mid]==target:
            return True
        elif nums[mid]<target: 
            left = mid+1
        else: 
            right = mid-1

    return False

nums = [1, 3, 4, 6]
print(binary_search_iter(nums, 5))

import bisect
def binary_search_module(nums, target):
    index = bisect.bisect_left(nums, target)
    if index<len(nums) and nums[index]==target:
        return True
    else:
        print(index)
        return False

nums = [1, 3, 4, 6]
print(binary_search_module(nums, 1))


