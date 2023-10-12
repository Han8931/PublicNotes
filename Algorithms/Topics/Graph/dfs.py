"""
Notes: 
- The graph structure is not included in the function definition.
- Start node is the input.
"""

graph = {
        1:[2,3,4],
        2:[5],
        3:[5],
        4:[],
        5:[6,7],
        6:[],
        7:[3],
        }


def dfs_rec(v, visited=[]):
    visited.append(v)

    for w in graph[v]:
        if w not in visited:
            visited = dfs_rec(w, visited)
    return visited

def dfs_rec2(v):
    visited = []
    
    def recursion(node):
        visited.append(node)
        for w in graph[node]:
            if w not in visited:
                recursion(w)

    recursion(v)

    return visited

def dfs_iter(start_v):
    visited = []

    # We have to first push the start node 
    # in the stack to start traversing
    stack = [start_v] 
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)

    return visited

print(dfs_rec(1))
print(dfs_rec2(1))
print(dfs_iter(1))
