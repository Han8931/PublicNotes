import heapq

def kth_largest_element_array(nums, k):
    heapq.heapify(nums)

    for _ in range(len(nums)-k):
        heapq.heappop(nums)

    return heapq.heappop(nums)

def kth_largest_element_array(nums, k):
    return sorted(nums, reverse=True)[k-1]

arr = [1,2,4,5]
print(kth_largest_element_array(arr, 3))
