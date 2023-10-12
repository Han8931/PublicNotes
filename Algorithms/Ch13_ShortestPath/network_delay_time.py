import pdb
import heapq
import collections

def network_delay(times, n, k):
    """
    Dijkstra algorithm
    """
    # Construct graph
    graph = collections.defaultdict(list) 
    for u, v, w in times:
        graph[u].append((v,w))

    Q = [(0,k)]
    dist = collections.defaultdict(int)

    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))

    return max(dist.values()) if len(dist)==n else -1

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

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(network_delay(times, n, k))
print(network_delay_bf(times, n, k))

