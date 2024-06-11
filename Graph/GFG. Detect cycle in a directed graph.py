# Detect cycle in a directed graph

# Optimal Solution(using DFS)

class Solution:
    def dfs(self, node, adj, vis, pathVis):
        # Mark the current node as visited
        vis[node] = 1
        # Mark the current node as part of the current path
        pathVis[node] = 1
        
        # Traverse all adjacent nodes
        for adj_node in adj[node]:
            # If the adjacent node is not visited, perform DFS on it
            if vis[adj_node] == 0:
                if self.dfs(adj_node, adj, vis, pathVis) == True:
                    return True
            # If the adjacent node is part of the current path, a cycle is detected
            elif pathVis[adj_node] == 1:
                return True
        
        # Unmark the current node as part of the current path
        pathVis[node] = 0
        return False
    
    # Function to detect cycle in a directed graph.
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        # Initialize the visited array with 0
        vis = [0] * V
        # Initialize the path visited array with 0
        pathVis = [0] * V
        
        # Check each node in the graph
        for i in range(V):
            # If the node is not visited, perform DFS to check for cycles
            if vis[i] == 0:
                if self.dfs(i, adj, vis, pathVis) == True:
                    return True
        # If no cycles were found, return False
        return False


# Time Complexity: O(V + E)
# Space Complexity: O(N)


# Optimal Solution (using BFS - using Kahn's Algorithm)
    
from typing import List
from collections import deque

class Solution:
    # Function to detect cycle in a directed graph.
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        # Initialize in-degree of all vertices as 0
        inDegree = [0] * V
        
        # Calculate in-degree of each vertex
        for i in range(V):
            for node in adj[i]:
                inDegree[node] += 1
                
        # Initialize the queue with all vertices having in-degree 0
        que = deque()
        for node in range(V):
            if inDegree[node] == 0:
                que.append(node)
        
        # Counter for visited vertices
        count = 0
        
        # Process vertices in the queue
        while que:
            node = que.popleft()
            count += 1
            
            # Decrease in-degree of adjacent vertices
            for adj_node in adj[node]:
                inDegree[adj_node] -= 1
                # If in-degree becomes 0, add it to the queue
                if inDegree[adj_node] == 0:
                    que.append(adj_node)
        
        # Check if topological sort includes all vertices
        if count == V:
            return False  # No cycle
        else:
            return True  # Cycle exists

    
# Time Complexity: O(V + E)
# Space Complexity: O(N)