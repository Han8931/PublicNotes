## Key Differences
-   __BFS finds the shortest path to the destination__, whereas __DFS goes to the bottom of a subtree, then backtracks__.
-   BFS uses a __queue__ to keep track of the next location to visit. whereas DFS uses a __stack__ to keep track of the next location to visit.
-   BFS traverses according to tree __level__, while DFS traverses according to tree __depth__.
-   In BFS, you can __never be trapped into finite loops__, whereas in DFS, you can be __trapped into infinite loops__.

 **Input:**
        A
       / \
      B   C
     /   / \
    D   E   F

## Depth First Search (DFS)
**DFS,** [**Depth First Search**](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/), is an edge-based technique. It uses the stack data structure and performs two stages, first visited vertices are pushed into the stack, and second if there are no vertices then visited vertices are popped.

Output: A, B, C, D, E, F

### DFS - Recursion
```python
def dfs_rec(v, discovered=[]):
    discovered.append(v)

    for w in graph[v]:
        if w not in discovered:
            discovered = dfs_rec(w, discovered)
    return discovered

```

### DFS - Iteration
* Visit and push to stack later.
 - __We want to search while going deeper, so we should not append all children to the visit list. We will append only the parent node and push the children to the stack first__


```python
def dfs_iter(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)

    return discovered

```


## Breadth First Search (BFS)
**BFS, Breadth-First Search,** is a vertex-based technique for finding the shortest path in the graph. It uses a [Queue data structure](https://www.geeksforgeeks.org/queue-data-structure/) that follows first in first out. In BFS, one vertex is selected at a time when it is visited and marked then its adjacent are visited and stored in the queue. It is slower than DFS.

Output: A, B, C, D, E, F

_Note that BFS cannot be implemented through recursion function._

```python
def bfs(start_v):
    visited = [start_v]
    queue = [start_v]

    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in visited:
                queue.append(w)
                visited.append(w)
    return visited
```












