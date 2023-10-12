"""
This question asks to find a longest palindrome substring in a sequence.
We can notice that two ends of a palindrome exptend and its size can be either of
1) even: bb > bbbb > bbbbbb : 2-4-6
2) odd: bcb > bbcbb > : 3-5-7
We need to consider both cases
"""
import pdb
import collections

s = "abccccdd"
#s = 'bb'
#s = 'abb'
#s = 'ccd'
#s = 'aaa'
#print(collections.Counter(s).values())

def longPalindrome(strs):
    if len(strs)<2 or strs==strs[::-1]:
        return strs

    def expand(left:int, right:int)->str:
        """
        s[left]==s[right]: Check palindrome
        """
        while left>=0 and right<len(strs) and strs[left]==strs[right]:
            left-=1
            right+=1
        return strs[left+1:right]

    result = ''
    for i in range(len(strs)-1):
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)
    return result

print(s)
print(longPalindrome(s))

