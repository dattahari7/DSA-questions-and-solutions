# Shortest Path in Weighted undirected graph

# Optimal Solution (using Dijkstra Algorithm)

import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        # Initialize adjacency list
        adj_list = [[] for _ in range(n)]
        for u, v, w in edges:
            adj_list[u-1].append((v-1, w))
            adj_list[v-1].append((u-1, w))
        
        # Initialize distance and parent arrays
        dist = [float('inf')] * n
        parent = [-1] * n
        dist[0] = 0
        parent[0] = 0
        
        # Priority queue to store (distance, node)
        pq = [(0, 0)]
        
        while pq:
            # Extract the node with the minimum distance
            curr_dist, curr_node = heapq.heappop(pq)
            
            # Skip processing if a shorter path to the current node was already found
            if curr_dist > dist[curr_node]:
                continue
            
            # Process each neighbor of the current node
            for adj_node, weight in adj_list[curr_node]:
                new_dist = curr_dist + weight
                # Update the shortest path if a new shorter path is found
                if new_dist < dist[adj_node]:
                    dist[adj_node] = new_dist
                    heapq.heappush(pq, (new_dist, adj_node))
                    parent[adj_node] = curr_node
        
        # If the destination node is unreachable, return [-1]
        if dist[n-1] == float('inf'):
            return [-1]
        
        # Reconstruct the shortest path from source to destination
        path = []
        node = n - 1
        while node != 0:
            path.append(node + 1)
            node = parent[node]
        
        # Add the source node to the path and reverse the path to get the correct order
        path.append(1)
        path.reverse()
        
        # Return the shortest path distance followed by the path itself
        return [dist[n-1]] + path


# Time Complexity: O(M * log N)
# Space Complexity: O(N)