# Floyd Warshall Algorithm


# Optimal Solution (using in-place)

class Solution:
    def shortest_distance(self, matrix):
        n = len(matrix)  # Number of vertices in the graph
        
        # Initialize the matrix:
        # Set -1 to infinity (inf) to indicate no direct path between nodes
        # Set diagonal elements to 0 (distance from a node to itself)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = float('inf')
                if i == j:
                    matrix[i][j] = 0

        # Implement the Floyd-Warshall algorithm:
        # This algorithm finds the shortest paths between all pairs of vertices
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # Update the shortest path from i to j through k
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
                    
        # After the algorithm, convert any remaining 'inf' values back to -1:
        # 'inf' indicates that no path exists between the nodes
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = -1


# Optimal Solution (using extra dist array)

def floyd_warshall(n, edges):
    # Initialize the distance matrix with infinity
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Distance from each node to itself is 0
    for i in range(n):
        dist[i][i] = 0
    
    # Fill the distance matrix with the given edges
    for u, v, w in edges:
        dist[u][v] = w

    # Update the distance matrix
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# Time Complexity: O(V3), as we have three nested loops each running for V times, where V = no. of vertices.

# Space Complexity: O(V2), where V = no. of vertices. This space complexity is due to storing the adjacency matrix of the given graph.

