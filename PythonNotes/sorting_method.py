"""
Various Sorting Methods:

TimSort
O(n)
"""

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

