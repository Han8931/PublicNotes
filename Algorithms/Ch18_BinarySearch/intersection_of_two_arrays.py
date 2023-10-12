import pdb

def intersection_bf(nums1, nums2):
    intersect = set()
    for n1 in nums1:
        for n2 in nums2:
            if n1==n2:
                intersect.add(n1)

    return intersect

def intersection_bs(nums1, nums2):
    intersect = set()

    nums2.sort()
    def binary_search(nums, target):
        left = 0
        right = len(nums)-1

        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]<target:
                left = mid+1
            elif nums[mid]>target:
                right = mid-1
            else:
                return True
        return False


    for n in nums1:
        if binary_search(nums2, n):
            intersect.add(n)
        
    return intersect

def intersection_two_pointer(nums1, nums2):
    intersect = set()
    nums1.sort()
    nums2.sort()

    i=j=0

    while i<len(nums1) and j<len(nums2):
        if nums1[i]>nums2[j]:
            j+=1
        elif nums1[i]<nums2[j]:
            i+=1
        else:
            intersect.add(nums1[i])
            i+=1
            j+=1
    return intersect


nums1 = [1]
nums2 = [1, 2]

print(intersection_bf(nums1, nums2))
print(intersection_bs(nums1, nums2))
print(intersection_two_pointer(nums1, nums2))
