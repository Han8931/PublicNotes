J = "aA"
S = "aAAbbbb"

import collections
import pdb

def numJewels(J, S):
    freqs = collections.defaultdict(int)
    count = 0

    for char in S:
        freqs[char]+=1

    for char in J:
        count+=freqs[char]

    return count

print(numJewels(J, S))

def numJewels2(J, S):
    freqs = collections.Counter(S)
    count = 0

    for char in J:
        count+=freqs[char]

    return count
    
print(numJewels2(J, S))

def numJewels3(J, S):
    return sum([s in J for s in S])

print(numJewels3(J, S))
