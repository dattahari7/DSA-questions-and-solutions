# Shortest path in Directed Acyclic Graph

# Optimal Solution (using DFS)

from typing import List
from collections import deque, defaultdict

class Solution:
    def dfs(self, node, adj_list, vis, stack):
        vis[node] = 1  # Mark the node as visited
        for adj_node, weight in adj_list[node]:  # Iterate through adjacent nodes and their weights
            if vis[adj_node] == 0:  # If the adjacent node is not visited
                self.dfs(adj_node, adj_list, vis, stack)  # Perform DFS on the adjacent node
        stack.append(node)  # Push the node to the stack after visiting all adjacent nodes
        
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)  # Initialize adjacency list for the graph
        for a, b, wth in edges:
            adj_list[a].append((b, wth))  # Add edge a -> b with weight wth
            
        vis = [0] * n  # Initialize visited array
        stack = deque()  # Initialize stack to store the topological order
        
        for i in range(n):
            if vis[i] == 0:  # If the node is not visited
                self.dfs(i, adj_list, vis, stack)  # Perform DFS to get the topological order
                
        dist = [float('inf')] * n  # Initialize distances with infinity
        dist[0] = 0  # Distance to the source node (node 0) is 0
        while stack:
            node = stack.pop()  # Get the node from the stack
            for adj_node, wth in adj_list[node]:  # Iterate through adjacent nodes and their weights
                if dist[node] + wth < dist[adj_node]:  # If a shorter path is found
                    dist[adj_node] = wth + dist[node]  # Update the distance
        
        for i in range(len(dist)):
            if dist[i] == float('inf'):  # If the node is not reachable
                dist[i] = -1  # Set the distance to -1
                
        return dist  # Return the list of shortest distances


# Time Complexity: O(V + E)
# Space Complexity: O(N + M)