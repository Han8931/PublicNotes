"""
BFS has no recursion
"""
import collections

graph = {
        1:[2,3,4],
        2:[5],
        3:[5],
        4:[],
        5:[6,7],
        6:[],
        7:[3],
        }

def bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)

    return discovered


print(bfs(1))
