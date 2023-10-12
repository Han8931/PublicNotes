### Permutations

![[Pasted image 20221021231231.png]]

Input: nums=[1, 2, 3]
Output: Res = [[1,2,3],....,]

```python
def permutation(nums):
    result = []
    prev_elements = []

    def dfs(elements):
        if not elements:
            result.append(prev_elements)

        for i in range(len(elements)):
            next_elements = elements[:]
            next_elements = next_elements[:i]+next_elements[i+1:]

            prev_elements.append(elements[i])
            print(prev_elements)

            dfs(next_elements)
            prev_elements.pop()
            print(f"Backtrack: {prev_elements}") 

    dfs(nums)
    return result
```

```python
[1]
[1, 2]
[1, 2, 3]
Backtrack: [1, 2]
Backtrack: [1]
[1, 3]
[1, 3, 2]
Backtrack: [1, 3]
Backtrack: [1]
Backtrack: []
[2]
[2, 1]
[2, 1, 3]
Backtrack: [2, 1]
Backtrack: [2]
[2, 3]
[2, 3, 1]
Backtrack: [2, 3]
Backtrack: [2]
Backtrack: []
[3]
[3, 1]
[3, 1, 2]
Backtrack: [3, 1]
Backtrack: [3]
[3, 2]
[3, 2, 1]
Backtrack: [3, 2]
Backtrack: [3]
Backtrack: []
```
