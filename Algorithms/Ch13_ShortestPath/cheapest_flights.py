import pdb
import collections
import heapq

edges = [[0,1,100], [1,2,100], [0,2,500]]

def findCheapestPrice(n, flights, src, dst, k):
    # Dijkstra algorithm version
    graph = collections.defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v,w))

    minHeap = [(0,src,k)]

    while minHeap:
        price, node, k = heapq.heappop(minHeap)

        if node==dst:
            return price

        if k>=0:
            for v, w in graph[node]:
                heapq.heappush(minHeap, (price+w, v, k-1))

    return -1

def findCheapestPriceBF(n, flights, src, dst, k):

    # Bellman-Ford Solution
    prices = [float("inf")]*n
    prices[src] = 0

    for i in range(k+1):
        tmpPrices = prices[:]
        for s, d, p in flights: # s:source, d: destination, p:price
            if prices[s] == float("inf"):
                continue
            if prices[s]+p<tmpPrices[d]:
                tmpPrices[d]=prices[s]+p

        prices = tmpPrices

    return -1 if prices[dst]==float("inf") else prices[dst]

print(findCheapestPriceBF(3, edges, 0, 1, 2))
            
