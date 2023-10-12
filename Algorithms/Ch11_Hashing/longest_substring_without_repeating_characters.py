"""
Sliding window with two pointers
There is one thing we have to care:
    The dictionary 'used' keeps all used chars so we need to make it sure that start point is always smaller than used index.
"""

import pdb
import sys
import time

#s = "bdned"

#s = "abcabcbb"
# s = "bbbbbb"
s = "pwwkew"

def longestSubStr(s:str)->int:
    used = {}
    max_len = start = 0

    for idx in range(len(s)):
        c = s[idx]

        if c in used and start<=used[c]:
        #if c in used:
            start=used[c]+1
        else:
            max_len = max(max_len, idx-start+1)
        used[c] = idx
            
    return max_len

start_t = time.perf_counter()
print(longestSubStr(s))
elapsed_time = time.perf_counter()-start_t
print(elapsed_time)





