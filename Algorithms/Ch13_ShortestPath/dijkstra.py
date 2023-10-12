import pdb
import heapq
import collections
import time


graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

def dijkstra(graph, source):
    """
    distances: keep the distances from the source to targets
    """
    dist = {v: float('inf') for v in graph}
    dist[source] = 0

    Q = [(0, source)]

    while Q:
        dist_v, v = heapq.heappop(Q)
        for u, dist_u in graph[v].items():
            new_dist = dist_v+dist_u
            if new_dist<dist[u]:
                dist[u] = new_dist
                heapq.heappush(Q, (new_dist, u))

    return dist

start = time.time()
print(dijkstra2(graph, 'A'))
end = time.time()
print(end-start)
