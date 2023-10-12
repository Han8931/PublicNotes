import pdb
from typing import List
import itertools

def permutations(nums):
    results = []
    prev_elements = []

    def dfs(elements):
        if len(elements)==0:
            results.append(prev_elements[:])
            return 

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)

    return results

#def permutations2(nums):
#    results = []
#    prev_elements = []
#
#    def dfs(elements):
#        if not elements:
#            results.append(prev_elements.copy())
#
#        for i in range(len(elements)):
#            next_elements = elements[:i].copy()+elements[i+1:].copy()
#            prev_elements.append(elements[i])
#            dfs(next_elements)
#            prev_elements.pop()
#    dfs(nums)
#
#    return results

#def permute(nums):
#    return list(itertools.permutations(nums))

nums = [1,2,3]

print(permutations(nums))

