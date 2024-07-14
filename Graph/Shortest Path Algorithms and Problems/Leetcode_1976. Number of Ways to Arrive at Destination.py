# 1976. Number of Ways to Arrive at Destination

# Optimal Solution (using Dijkstra Algorithm)

from collections import defaultdict
import heapq
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Initialize graph as an adjacency list
        graph = defaultdict(list)
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        # Initialize times array with infinity, and ways array with 0
        times = [float('inf')] * n
        times[0] = 0  # Starting point time is 0
        ways = [0] * n
        ways[0] = 1  # There is one way to reach the starting point

        # Priority queue to manage the current shortest path candidates
        pq = [(0, 0)]  # (time, node)

        while pq:
            old_t, u = heapq.heappop(pq)  # Get the node with the smallest time

            # Explore all adjacent nodes
            for v, t in graph[u]:
                new_t = old_t + t  # Calculate new time to reach node v
                if new_t < times[v]:  # If new time is shorter, update shortest path
                    heapq.heappush(pq, (new_t, v))  # Push new time and node to priority queue
                    times[v] = new_t  # Update shortest time to reach node v
                    ways[v] = ways[u]  # Update ways to reach node v with ways to reach node u
                elif new_t == times[v]:  # If new time is equal to current shortest time
                    ways[v] += ways[u]  # Add the number of ways to reach node u to ways to reach node v

        mod = 10 ** 9 + 7  # Modulo value for the result
        return ways[-1] % mod  # Return the number of ways to reach the last node, modulo 10^9 + 7


# Time Complexity: O((V + E)log(v)) Where E = Number of edges and V = Number of Nodes.
# Space Complexity: O(E + V) Where E = Number of edges and V = Number of Nodes.