def longestPalindrome(self, strs: str) -> int:
    count = collections.Counter(strs)

    length = 0
    for key, item in count.items():
        if item%2==0:
            length+=item
        else:
            length+=(item-1)
        
    return min(length+1, len(strs))
