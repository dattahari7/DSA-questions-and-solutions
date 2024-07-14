# Bellman-Ford Algorithm

class Solution:
    def bellman_ford(self, V, edges, S):
        """
        Function to implement the Bellman-Ford algorithm to find the shortest path from a single source to all other vertices in a given weighted graph.
        
        Args:
        V (int): Number of vertices in the graph.
        edges (List[Tuple[int, int, int]]): List of edges in the graph, each edge is represented as a tuple (u, v, w) where u is the source vertex, v is the destination vertex, and w is the weight of the edge.
        S (int): Source vertex from which to calculate shortest paths.

        Returns:
        List[int]: List of shortest distances from the source to each vertex. If a negative-weight cycle is detected, returns [-1].
        """
        # Define a large number representing infinity for initial distances
        inf = 100000000
        
        # Initialize distance to all vertices as infinity and distance to the source as 0
        dist = [inf] * V
        dist[S] = 0
        
        # Relax all edges V-1 times
        for _ in range(V - 1):
            for u, v, w in edges:
                # If the current distance to u is not infinity and the distance to v through u is shorter
                if dist[u] != inf and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Check for negative-weight cycles by trying to relax the edges one more time
        for u, v, w in edges:
            if dist[u] != inf and dist[u] + w < dist[v]:
                # If we can still relax an edge, then there is a negative-weight cycle
                return [-1]
        
        # Return the list of shortest distances
        return dist



# Time Complexity: O(V*E), where V = no. of vertices and E = no. of Edges.

# Space Complexity: O(V) for the distance array which stores the minimized distances.