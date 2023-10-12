import pdb
import collections

# Sequence Unpacking Operator

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4]
c = [1, 2, 3]

# In Python3, zip function returns a generator
print(zip(a,b))

# To print it as a list, then 
print(list(zip(a,b)))
print(list(zip(a,b,c)))

# zip outputs a tuple which is immutable so we cannot change its value.

print(list(zip(a)))

# Collections
print("Collections")
nums = [4, 4, 2, 2, 2, 5]
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

def print_func(*param):
    print(param)

print_func('a', 'b', 'c')

a, *b = [1, 2, 3, 4]
print(a)
print(b)

date_info = {"year":2000, "month": '01', "day": 7}
new_info = {**date_info, "day":14}
print(new_info)


