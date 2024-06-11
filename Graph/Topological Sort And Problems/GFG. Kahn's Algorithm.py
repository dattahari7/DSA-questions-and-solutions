# Kahn's Algorithm (Topological Sort using BFS)

# Optimal Solution

from collections import deque

class Solution:
    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Initialize in-degree of all vertices as 0
        inDegree = [0] * V
        
        # Calculate in-degree of each vertex
        for i in range(V):
            for node in adj[i]:
                inDegree[node] += 1
        
        # Initialize the queue with all vertices having in-degree 0
        que = deque()
        for i in range(V):
            if inDegree[i] == 0:
                que.append(i)
                
        # Initialize list to store the topological order
        topo = []
        
        # Process vertices in the queue
        while que:
            node = que.popleft()
            topo.append(node)
            
            # Decrease in-degree of adjacent vertices
            for adj_node in adj[node]:
                inDegree[adj_node] -= 1
                
                # If in-degree becomes 0, add it to the queue
                if inDegree[adj_node] == 0:
                    que.append(adj_node)
        
        return topo


# Time Complexity: O(V + E)
# Space Complexity: O(N)