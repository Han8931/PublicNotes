import time
from datetime import timedelta
import collections
import pdb
import re

"""
isalnum: is alphanumeric?
"""

def palindrome(x):
    return False if x<0 else x==int(str(x)[::-1])

def isPalindrome(s: str) -> bool:
    # Note that we cannot use [^\w], since \w matches underscores '_'
    s = re.sub('[^a-zA-Z0-9]',"", s).lower()
    return s[::]==s[::-1]

def palindrome2(chars):
    strs = []
    for char in chars:
        if char.isalnum(): 
            strs.append(char.lower())

    return True if strs==strs[::-1] else False

def palindrome3(chars):
    strs = []
    for char in chars:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs)>1:
        # pop the first one and remove the first item 
        # pop the last one and remove the last item 
        if strs.pop(0)!=strs.pop():
            return False

    return True

def palindrome4(chars):
    strs:Deque = collections.deque()

    for char in chars:
        if char.isalnum(): 
            strs.append(char.lower())

    while len(strs)>1:
        # pop the first one and remove the first item 
        # pop the last one and remove the last item 
        if strs.popleft()!=strs.pop():
            return False

    return True


start_t_gen = time.perf_counter()
print(palindrome(121))
eval_t = time.perf_counter()-start_t_gen
print(f"Total Elapsed Time: {timedelta(seconds=eval_t)}", flush=True) 

start_t_gen = time.perf_counter()
print(palindrome2("goog"))
eval_t = time.perf_counter()-start_t_gen
print(f"Total Elapsed Time: {timedelta(seconds=eval_t)}", flush=True) 

start_t_gen = time.perf_counter()
print(palindrome3("goog"))
eval_t = time.perf_counter()-start_t_gen
print(f"Total Elapsed Time: {timedelta(seconds=eval_t)}", flush=True) 

start_t_gen = time.perf_counter()
print(palindrome4("goog"))
eval_t = time.perf_counter()-start_t_gen
print(f"Total Elapsed Time: {timedelta(seconds=eval_t)}", flush=True) 
