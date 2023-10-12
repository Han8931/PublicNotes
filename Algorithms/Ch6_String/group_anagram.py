"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

import pdb
import time
from datetime import timedelta

import collections

strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagram(strs):
    anagrams = collections.defaultdict(list)
    for word in strs:
        # Approach to a list with key and append word to the list
        anagrams["".join(sorted(word))].append(word)
    return anagrams.values()


start_t_gen = time.perf_counter()
print(groupAnagram(strs))
eval_t = time.perf_counter()-start_t_gen
print(f"Total Elapsed Time: {timedelta(seconds=eval_t)}", flush=True) 




