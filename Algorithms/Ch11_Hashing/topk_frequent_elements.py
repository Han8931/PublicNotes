import pdb
import collections

nums = [1,1,1,4,4,3]
def topkElements(nums, k):
    return list(zip(*collections.Counter(nums).most_common(k)))[0]

print(topkElements(nums, 2))


