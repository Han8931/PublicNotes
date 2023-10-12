def single_number(nums):
    result = 0
    for n in nums:
        result ^= n
    return result

nums = [1, 2, 1, 2, 3]
print(single_number(nums))
