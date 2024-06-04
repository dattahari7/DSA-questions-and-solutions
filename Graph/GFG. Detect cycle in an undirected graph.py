# Detect cycle in an undirected graph

# Optimal Solution(using BFS)

from typing import List
from collections import deque

class Solution:
    # Helper function to detect a cycle starting from the source node
    def detectCycle(self, src, adj, visited):
        # Initialize a queue for BFS with the source node and its parent as -1
        que = deque([(src, -1)])
        # Mark the source node as visited
        visited[src] = True
        
        while que:
            # Pop the current node and its parent from the queue
            curr_node, parent_node = que.popleft()
            
            # Iterate through all adjacent nodes of the current node
            for adjacent_node in adj[curr_node]:
                # If the adjacent node has not been visited, add it to the queue with the current node as its parent
                if visited[adjacent_node] == False:
                    que.append((adjacent_node, curr_node))
                    visited[adjacent_node] = True
                # If the adjacent node is visited and is not the parent of the current node, a cycle is detected
                elif parent_node != adjacent_node:
                    return True
        # Return False if no cycle is detected
        return False
    
    # Function to detect a cycle in an undirected graph
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        # Initialize a visited list to keep track of visited nodes
        visited = [False] * V
        
        # Iterate through all nodes in the graph
        for node in range(V):
            # If the node has not been visited, check for a cycle starting from that node
            if visited[node] == False:
                if self.detectCycle(node, adj, visited) == True:
                    return True
        # Return False if no cycle is detected in the entire graph
        return False


# Time Complexity: O(N * 2E) here E is total degree of graph
# Space Complexity: O(N)


# Optimal Solution(using DFS)

from typing import List

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        # Inner function to perform DFS and check for cycles
        def dfs(curr_node, parent_node, vis, adj):
            # Mark the current node as visited
            vis[curr_node] = 1
            
            # Iterate through all adjacent nodes
            for adjacent_node in adj[curr_node]:
                # If the adjacent node is not visited, recursively perform DFS
                if vis[adjacent_node] == 0:
                    if dfs(adjacent_node, curr_node, vis, adj):
                        return True
                # If the adjacent node is visited and is not the parent, a cycle is detected
                elif adjacent_node != parent_node:
                    return True
            # Return False if no cycle is detected
            return False
        
        # Initialize the visited list with 0 (indicating unvisited nodes)
        vis = [0] * V
        # Iterate through all nodes
        for node in range(V):
            # If the node is not visited, perform DFS from that node
            if vis[node] == 0:
                if dfs(node, -1, vis, adj):
                    return True
        # Return False if no cycle is detected in the entire graph
        return False


# Time Complexity: O(N * 2E)
# Space Complexity: O(N) 