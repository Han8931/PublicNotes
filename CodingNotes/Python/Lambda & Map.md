---
tags:python
---

```python
func = lambda x: (x.split()[1], x.split()[0])
letters.sort(key=func)
```

```python
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry')) 
```
