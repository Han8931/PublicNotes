
```python
def network_delay_bf(times, n, k):
    """
    Bellman-Ford algorithm
    """
    # Construct graph
    dist = [float('inf')]*n
    dist[k-1] = 0

    for _ in range(n-1):
        for u, v, w in times:
            if dist[u-1]+w<dist[v-1]:
                dist[v-1] = dist[u-1]+w

    return max(dist) if max(dist)< float("inf") else -1
```