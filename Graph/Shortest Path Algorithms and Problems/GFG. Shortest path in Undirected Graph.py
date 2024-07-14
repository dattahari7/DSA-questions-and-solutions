# Shortest path in Undirected Graph

# Optimal Solution (using BFS)

from collections import deque, defaultdict

class Solution:
    def shortestPath(self, edges, n, m, src):
        # Initialize adjacency list for the graph
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)  # Add edge a -> b
            adj_list[b].append(a)  # Add edge b -> a
            
        # Initialize distances with infinity
        dist = [float('inf')] * n
        dist[src] = 0  # Distance to the source is 0
        que = deque([src])  # Initialize queue with the source node
        
        while que:
            node = que.popleft()  # Dequeue a node
            for adj_node in adj_list[node]:  # Iterate through adjacent nodes
                if dist[node] + 1 < dist[adj_node]:  # Check if a shorter path is found
                    dist[adj_node] = 1 + dist[node]  # Update distance
                    que.append(adj_node)  # Enqueue the adjacent node
                    
        # Replace infinity with -1 to indicate unreachable nodes
        res = [dist[i] if dist[i] != float('inf') else -1 for i in range(n)]
        
        return res


# Time Complexity: O(V + 2E)
# Space Complexity: O(N + M)