# First Solution

![[Pasted image 20230927190452.png | 700]]


# Second Solution

![[Pasted image 20230928105041.png]]

```python
def subsets(nums):
    result = []

    def recursion(index, path):
        result.append(path)

        for i in range(index, len(nums)):
            recursion(i+1, path+[nums[i]])

    recursion(0, [])
    return result
```



