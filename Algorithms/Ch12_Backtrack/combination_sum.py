import pdb

def combSum(candidates, target):
    res = []
    prev_elements = []

    def dfs(candidates):
        s = sum(prev_elements)
        if s==target:
            res.append(prev_elements[:])
        elif s>target:
            return 

        for i in range(len(candidates)):
            next_cand = candidates[:]

            prev_elements.append(candidates[i])
            dfs(next_cand[i:])
            prev_elements.pop()

    dfs(candidates)
    return res

def combSum2(candidates, target):
    res = []

    def dfs(csum, index, path):
        if csum<0:
            return 
        if csum ==0:
            res.append(path)
            return 

        for i in range(index, len(candidates)):
            dfs(csum-candidates[i], i, path+[candidates[i]])

    dfs(target, 0, [])
    return result

candidates = [2, 3, 6, 7]
print(combSum(candidates, 7))

#candidates = [2, 3, 5]
#print(combSum(candidates, 8))

