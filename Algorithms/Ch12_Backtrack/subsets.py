import time, datetime

# Best
def subsets(nums):
    result = []

    def recursion(index, path):
        result.append(path)

        for i in range(index, len(nums)):
            recursion(i+1, path+[nums[i]])

    recursion(0, [])
    return result

def subsets2(nums):
    res = []
    subset = []
    def dfs(i):
        if i>=len(nums):
            res.append(subset[:])
            return

        subset.append(nums[i])
        dfs(i+1)
        subset.pop()
        dfs(i+1)

    dfs(0)
    return res

def subset(arr):
    results = []
    prev_elem = []

    def recursion(elements):
        if not len(elements)<0:
            results.append(prev_elem[:])

        for i in range(len(elements)):
            prev_elem.append(elements[i])
            recursion(elements[i+1:])
            prev_elem.pop()

    recursion(arr)
    return results

nums = [1,2,3]

start_t = time.perf_counter()
print(subset(nums))
elapsed_t = time.perf_counter() - start_t
print(f"{subsets.__name__}: {datetime.timedelta(elapsed_t)}")

start_t = time.perf_counter()
print(subsets2(nums))
elapsed_t = time.perf_counter() - start_t
print(f"{subsets.__name__}: {datetime.timedelta(elapsed_t)}")

start_t = time.perf_counter()
print(subsets(nums))
elapsed_t = time.perf_counter() - start_t
print(f"{subsets.__name__}: {datetime.timedelta(elapsed_t)}")


