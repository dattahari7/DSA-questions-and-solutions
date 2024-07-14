# 1192. Critical Connections in a Network

# Optimal Solution (using DFS)

from collections import defaultdict
from typing import List

class Solution:
    def __init__(self):
        # Initialize timer to track discovery times
        self.timer = 0

    def dfs(self, node, parent, vis, adj, disc, low, bridges):
        # Mark the current node as visited
        vis[node] = 1
        # Initialize discovery and low values
        disc[node] = low[node] = self.timer
        self.timer += 1
        
        # Explore all adjacent nodes
        for neighbor in adj[node]:
            # Skip the parent node
            if neighbor == parent:
                continue
            # If the neighbor is not visited, perform DFS on it
            if vis[neighbor] == 0:
                self.dfs(neighbor, node, vis, adj, disc, low, bridges)
                # Update the low value of the current node
                low[node] = min(low[node], low[neighbor])
                # Check if the edge is a bridge
                if low[neighbor] > disc[node]:
                    bridges.append([node, neighbor])
            else:
                # Update the low value if the neighbor is already visited
                low[node] = min(low[node], disc[neighbor])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Create adjacency list for the graph
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        # Initialize visited array, discovery times, and low values
        vis = [0] * n
        disc = [0] * n
        low = [0] * n
        bridges = []

        # Perform DFS starting from the first node
        self.dfs(0, -1, vis, adj, disc, low, bridges)
        
        # Return the list of bridges (critical connections)
        return bridges


# Time Complexity: O(V+2E), where V = no. of vertices, E = no. of edges. It is because the algorithm is just a simple DFS traversal.

# Space Complexity: O(V+2E) + O(3V), where V = no. of vertices, E = no. of edges. O(V+2E) to store the graph in an adjacency list and O(3V) for the three arrays i.e. tin, low, and vis, each of size V.