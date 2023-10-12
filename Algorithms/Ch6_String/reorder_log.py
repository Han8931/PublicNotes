"""
Reorder Data in Log Files
- isdigit
"""

import pdb

#Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
#Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

def reorderData(logs):
    letters = []
    digits = []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    func = lambda x: (x.split()[1], x.split()[0])
    letters.sort(key=func)

    return letters+digits

print(reorderData(logs))


