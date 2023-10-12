"""
Most Common Word

Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
"""

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


import re
import collections

def mostCommonWord(paragraph, banned):
    words = [word for word in re.sub('[\W]', ' ', paragraph).lower().split() if word not in banned]
    counts = collections.Counter(words)

    return counts.most_common(1)[0][0] # [(ball, 2)]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["bob", "hit"]

print(mostCommonWord(paragraph, banned))
