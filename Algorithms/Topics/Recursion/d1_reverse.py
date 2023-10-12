import pdb
import time

def reverseString(string):
    l_cur = 0
    r_cur = len(string)-1

    while l_cur<r_cur:
        string[l_cur], string[r_cur] = string[r_cur], string[l_cur]
        l_cur+=1
        r_cur-=1
    return string

def reverseStringRecursive(string):
    l_cur = 0
    r_cur = len(string)-1

    if len(string)<2:
        return string
    else:
        return list(string[r_cur])+reverseStringRecursive(string[l_cur+1:r_cur])+list(string[l_cur])

def reverse_str(strs):
    right = len(strs)-1

    def reverse(right):
        if right>0:
            return strs[right]+reverse(right-1)
        else:
            return strs[0]
    return reverse(right)

print(reverseString(list("abcde")))

# start_t = time.perf_counter()
# print(reverseString(list("abcde")))
# elapsed_time = time.perf_counter()-start_t
# print(elapsed_time)

# start_t = time.perf_counter()
# print(reverseStringRecursive(list("abcde")))
# elapsed_time = time.perf_counter()-start_t
# print(elapsed_time)

# start_t = time.perf_counter()
# print(reverse_str("abcde"))
# elapsed_time = time.perf_counter()-start_t
# print(elapsed_time)


