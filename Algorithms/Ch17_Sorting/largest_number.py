import sys
import pdb

def largest_number_fn(arr):

    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if int(str(str(arr[j-1])+str(arr[j])))<int(str(str(arr[j])+str(arr[j-1]))):
                arr[j], arr[j-1] = arr[j-1], arr[j] 

    return "".join(map(str, arr))

test = [3, 30, 34, 5, 9]
print(largest_number_fn(test))

