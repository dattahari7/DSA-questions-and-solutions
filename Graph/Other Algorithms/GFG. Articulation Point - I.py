# Articulation Point - I

# Optimized Solution (using DFS)

class Solution:
    def __init__(self):
        # Initialize timer for tracking discovery times
        self.timer = 1
    
    def dfs(self, node, parent, adj, vis, disc, low, mark):
        # Mark the current node as visited
        vis[node] = 1
        # Set discovery and low values
        disc[node] = low[node] = self.timer
        self.timer += 1
        # Initialize the count of children
        child = 0
        
        # Iterate through all adjacent nodes
        for adj_node in adj[node]:
            # Skip the parent node
            if adj_node == parent:
                continue
            
            if vis[adj_node] == 0:
                # If adjacent node is not visited, perform DFS on it
                self.dfs(adj_node, node, adj, vis, disc, low, mark)
                # Update the low value of the current node
                low[node] = min(low[node], low[adj_node])
                
                # If the adjacent node's low value is greater than or equal to the discovery value of the current node
                if low[adj_node] >= disc[node] and parent != -1:
                    mark[node] = 1
                
                # Increment the count of children
                child += 1
            else:
                # If adjacent node is already visited, update the low value
                low[node] = min(low[node], disc[adj_node])
        
        # If the current node is the root and has more than one child, mark it as an articulation point
        if child > 1 and parent == -1:
            mark[node] = 1
    
    def articulationPoints(self, V, adj):
        # Initialize arrays to keep track of visited nodes, discovery times, low values, and articulation points
        vis = [0] * V
        disc = [0] * V
        low = [0] * V
        mark = [0] * V
        
        # Perform DFS for each unvisited node
        for i in range(V):
            if vis[i] == 0:
                self.dfs(i, -1, adj, vis, disc, low, mark)
        
        # Collect all articulation points
        res = [i for i in range(V) if mark[i] == 1]
        
        # Return the articulation points or [-1] if none are found
        return res if res else [-1]


# Time Complexity: O(V+2E), where V = no. of vertices, E = no. of edges. It is because the algorithm is just a simple DFS traversal.
# Space Complexity: O(3V), where V = no. of vertices. O(3V) is for the three arrays i.e. tin, low, and vis, each of size V.