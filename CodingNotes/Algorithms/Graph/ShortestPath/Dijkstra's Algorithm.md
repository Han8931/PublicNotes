Given a graph and a source vertex (starting) in the graph, find the **shortest paths** from the source to all vertices in the given graph.

```python
graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}
```

```python
def dijkstra(graph, source):
    """
	- Dijkstra's algorithm is similar to BFS
	- However, we want to first search the edge with minimum length
    - Thus, we are gonna use MinHeap, which has log(n) cost. 
    - distances: keep the distances from the source to targets
    """
    dist = {v: float('inf') for v in graph}
    dist[source] = 0

    Q = [(0, source)]

    while Q:
        dist_v, v = heapq.heappop(Q)

		# We are gonna check the neighbors first.
        for u, dist_u in graph[v].items():
            new_dist = dist_v+dist_u
            if new_dist<dist[u]:
                dist[u] = new_dist
                heapq.heappush(Q, (new_dist, u))

    return dist

print(dijkstra(graph, 'A'))
```

