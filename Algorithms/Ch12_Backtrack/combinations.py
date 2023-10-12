import pdb

def combinations2(n, k):
    #nums = [i for i in ]
    return list(itertools.combinations(range(1,n+1), k))

# Best Option 
def combinations(n, k):
    res = []
    prev_elem = []

    def dfs(start, k):
        if k==0:
            res.append(prev_elem[:])
            return 
        for i in range(start, n+1):
            prev_elem.append(i)
            dfs(i+1, k-1)
            prev_elem.pop()

    dfs(1, k)
    return res

def combination(n:int, k:int)->list:

    results = []
    start = 0

    def recursion(elements, start, k):
        if k==0:
            results.append(elements[:])
            return 

        for i in range(start, n+1):
            elements.append(i)
            recursion(elements, i+1, k-1)
            elements.pop()

    recursion([], 1, k)
    return results


def combinations2(n,k):
    comb = []
    temp = []

    def dfs(start):
        if len(temp)==k:
            comb.append(temp[:])
        elif len(temp)>k:
            return

        for i in range(start,n+1):
            temp.append(i)
            dfs(i+1)
            temp.pop()

    dfs(1)
    return comb

print(combinations(3, 2))

