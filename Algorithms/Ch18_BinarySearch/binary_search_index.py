
def binary_search_index_rec(nums, target):
    def binary_split(left, right):
        if left<=right:
            mid = left+(right-left)//2
            if nums[mid]<target:
                left = mid+1
                return binary_split(left, right)
            elif nums[mid]>target:
                right = mid-1
                return binary_split(left, right)
            else:
                return mid
        else:
            return -1

    return binary_split(0, len(nums)-1)

def binary_search_index_iter(nums, target):
    left = 0
    right = len(nums)-1

    while left<=right:
        mid = left+(right-left)//2

        if nums[mid]==target:
            return mid
        elif nums[mid]<target: 
            left = mid+1
        else: 
            right = mid-1

    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9

print(binary_search_index_rec(nums, target))
print(binary_search_index_iter(nums, target))






