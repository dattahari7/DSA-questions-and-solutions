# Minimum Spanning Tree

# Optimal Solution (using Prim's algorithm)

import heapq

class Solution:
    
    # Function to find the sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        # Initialize a visited list to keep track of visited nodes
        vis = [0] * V
        # Priority queue (min-heap) to store the edges with their weights
        pq = [(0, 0)]
        
        # Variable to store the sum of weights of the MST
        sum_wth = 0
        
        # Continue until the priority queue is empty
        while pq:
            # Pop the edge with the smallest weight
            curr_wth, curr_node = heapq.heappop(pq)
            
            # If the node has already been visited, skip it
            if vis[curr_node] == 1:
                continue
            
            # Mark the node as visited
            vis[curr_node] = 1
            # Add the weight of the current edge to the total sum
            sum_wth += curr_wth
            
            # Traverse all adjacent nodes
            for adj_node, edw in adj[curr_node]:
                # If the adjacent node has not been visited, add it to the priority queue
                if vis[adj_node] != 1:
                    heapq.heappush(pq, (edw, adj_node))
                    
        return sum_wth


# Time Complexity: O(ElogV), where E is the number of edges and V is the number of vertices.
# Space Complexity: O(E+V) for the adjacency list and the priority queue.


# Optimal Solution (using Kruskal's Algorithm)

class DisjointSet:
    def __init__(self, n):
        # Initialize rank, parent, and size arrays
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find_u_par(self, node):
        # Find the ultimate parent of a node with path compression
        if node == self.parent[node]:
            return node
        # Path compression step
        self.parent[node] = self.find_u_par(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, u, v):
        # Union by rank
        ulp_u = self.find_u_par(u)  # Find ultimate parent of u
        ulp_v = self.find_u_par(v)  # Find ultimate parent of v
        if ulp_u == ulp_v:
            return
        # Attach the smaller rank tree under the root of the higher rank tree
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def union_by_size(self, u, v):
        # Union by size
        ulp_u = self.find_u_par(u)  # Find ultimate parent of u
        ulp_v = self.find_u_par(v)  # Find ultimate parent of v
        if ulp_u == ulp_v:
            return
        # Attach the smaller size tree under the root of the larger size tree
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

class Solution:
    def spanningTree(self, V, adj):
        # List to store all edges in the graph
        edges = []
        # Convert adjacency list to edge list
        for i in range(V):
            for it in adj[i]:
                adjNode = it[0]
                wt = it[1]
                node = i
                edges.append((wt, node, adjNode))

        # Initialize disjoint set
        ds = DisjointSet(V)
        # Sort edges based on weight
        edges.sort()
        # Initialize MST weight
        mstWt = 0
        # Process edges in sorted order
        for wt, u, v in edges:
            # If u and v are in different sets, include this edge in MST
            if ds.find_u_par(u) != ds.find_u_par(v):
                mstWt += wt
                # Perform union operation to include the edge in MST
                ds.union_by_size(u, v)

        return mstWt


# Time Complexity: O(ElogE), where E is the number of edges.
# Space Complexity: O(E+V)