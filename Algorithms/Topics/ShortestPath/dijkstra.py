import pdb
import heapq
import collections

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

# source: starting vertex
def dijkstra(graph, source):
    """
    distances: keep the distances from the source to targets
    """

    # Init all distances from source to nodes (vertices) as zero
    distances = {v: float('inf') for v in graph}
    distances[source] = 0  # Starting point value has to be 0

    # Create a priority queus by using heapq (min heap).
    # A Min Heap Binary Tree is a Binary Tree where the root node has the minimum key in the tree.
    queue = []

    # Push: [dist, vertex]
    heapq.heappush(queue, [distances[source], source])  # 

    while queue:

        # pop distance and vertex to visit
        curr_dist, curr_v = heapq.heappop(queue) 

        if distances[curr_v] < curr_dist:  
            continue

        for next_v, next_dist in graph[curr_v].items():
            dist_ = curr_dist + next_dist  
            if dist_ < distances[next_v]:  
                distances[next_v] = dist_
            heapq.heappush(queue, [dist_, next_v])  

    return distances

print(dijkstra(graph, 'A'))

def dijkstra2(graph, source):

    # Need to push a weight first to allow meanHeap sort.
    minHeap = [(0, source)] 
    edges = collections.defaultdict(int)

    while minHeap:
        w1, n1 = heapq.heappop(minHeap)

        if n1 not in edges:
            edges[n1] = w1

            for n2, w2 in graph[n1].items():
                heapq.heappush(minHeap, [w1+w2, n2])
    return edges


print(dijkstra3(graph, 'A'))


