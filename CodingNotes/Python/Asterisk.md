---
tags:python 
---
## zip function
- In Python3, zip function returns a generator
- zip outputs a tuple which is immutable so we cannot change its value.
- The input of zip function can be one or multiple

```python
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4]
c = [1, 2, 3]

# In Python3, zip function returns a generator
print(zip(a,b))

# To print it as a list, then 
print(list(zip(a,b))) # [(1, 1), (2, 2), (3, 3), (4, 4)]
print(list(zip(a,b,c))) # [(1, 1, 1), (2, 2, 2), (3, 3, 3)]

# zip outputs a tuple which is immutable so we cannot change its value.
```

## Asterisk

### Sequence Unpacking Operator
In python \* is a _sequence unpacking operator_.

```python
import collections

nums = [1,1, 2, 2, 2]
out = list(collections.Counter(nums).most_common(2))
print(out) # [(2, 3), (1, 2)]

# Unpacking
out = list(zip(*collections.Counter(nums).most_common(2)))
print(out) # [(2, 1), (3, 2)]

# Without Unpacking
out = list(zip(collections.Counter(nums).most_common(2)))
print(out) # [((2, 3),), ((1, 2),)]

fruits = ["lemon", "pear", "watermelon", "tomato"]
print(fruits) # ['lemon', 'pear', 'watermelon', 'tomato']
print(*fruits) # lemon pear watermelon tomato
```

### Packing operator in Function

```python
def print_func(*param):
    print(param)

print_func('a', 'b', 'c')
>>> ('a', 'b', 'c')
```

As shown in the above example, we have passed three params but they are packed as a single `param` variable.

### Asterisk in Variable Assignment

```python
a, *b = [1, 2, 3, 4]
print(a)
print(b)
```

### Double Asterisk: Key-Value Unpacking in Dictionaries

```python
date_info = {"year":2000, "month": '01', "day": 7}
new_info = {**date_info, "day":14}
print(new_info)
```












