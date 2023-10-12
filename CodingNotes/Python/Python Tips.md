---
tags:python
---

#### Max, Min
```python
import sys

min = sys.maxsize
max = -sys.maxsize
```

#### Create a defaultdict
`defaultdict` can avoid key collision of hash map.
```python
import collections
anagram_dict = collections.defaultdict(list)
```

#### Sorting

```python
a = [2, 5, 1, 9, 7]
print(sorted(a))

b = "zdkjfae"
print(sorted(b))

# In-place sort
a.sort()
print(a)

# Sort with a key

c = ['ccc', 'aa', 'd', 'bb']
print(sorted(c, key=len))

c = ['abc', 'cfc', 'cde']
print(sorted(c, key=lambda x: (x[0], x[-1])))
```

#### Countings

```python
import collections
collections.Counter(paragraph).most_common(1)[0][0] #[('ball', 2)]
```

