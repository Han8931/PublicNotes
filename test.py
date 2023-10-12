import pdb
import collections

import collections

nums = [1, 1, 2, 2, 2]
out = list(collections.Counter(nums).most_common(2))
print(out)

# Unpacking
out = list(zip(*collections.Counter(nums).most_common(2)))
print(out)

# Without Unpacking
out = list(zip(collections.Counter(nums).most_common(2)))
print(out)


fruits = ["lemon", "pear", "watermelon", "tomato"]
print(fruits)
print(*fruits)

