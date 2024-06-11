# Topological sort

# Optimal Solution (using DFS)

from collections import deque

class Solution:
    def dfs(self, node, adj, vis, stack):
        # Mark the current node as visited
        vis[node] = 1
        
        # Visit all the adjacent nodes
        for adj_node in adj[node]:
            if vis[adj_node] == 0:
                # Recursively perform DFS on the unvisited adjacent node
                self.dfs(adj_node, adj, vis, stack)
        
        # Once all adjacent nodes are processed, push the current node to the stack
        stack.append(node)

    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Initialize the visited array with 0
        vis = [0] * V
        # Initialize an empty deque to store the topological order
        stack = deque()
        
        # Perform DFS from each node
        for i in range(V):
            if vis[i] == 0:
                self.dfs(i, adj, vis, stack)
        
        # Prepare the result list from the stack
        res = []
        while stack:
            res.append(stack.pop())
        
        return res


# Time Complexity: O(V + E)
# Space Complexity: O(N)
    


# Optimal Solution (using BFS - Kahn's Algorithm)


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
