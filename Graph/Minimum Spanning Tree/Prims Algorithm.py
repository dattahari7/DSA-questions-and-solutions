# Prim's Algorithm

import heapq
from collections import defaultdict

def prim_mst(n, edges):
    if n == 0:
        return []

    # Adjacency list representation
    adj_list = defaultdict(list)
    for u, v, w in edges:
        adj_list[u].append((w, v))
        adj_list[v].append((w, u))

    # Priority queue to store the next edge to be considered
    min_heap = [(0, 0)]  # (weight, vertex)
    total_cost = 0
    mst = []
    visited = set()

    while min_heap and len(visited) < n:
        # Pop the smallest weight edge from the heap
        weight, u = heapq.heappop(min_heap)
        # If the node has already been visited, skip it
        if u in visited:
            continue
        # Mark the node as visited
        visited.add(u)
        # Add the weight of the edge to the total cost
        total_cost += weight
        # Add the node to the MST
        mst.append(u)

        # For each adjacent node, if it's not visited, add the edge to the heap
        for next_weight, v in adj_list[u]:
            if v not in visited:
                heapq.heappush(min_heap, (next_weight, v))

    # Return the MST if all nodes were visited, otherwise return an empty list
    return mst if len(visited) == n else []

# Example usage:
n = 5
edges = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]
print(prim_mst(n, edges))


# Time Complexity: O(ElogV), where E is the number of edges and V is the number of vertices.
# Space Complexity: O(E+V) for the adjacency list and the priority queue.