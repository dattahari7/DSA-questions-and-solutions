# Kruskal's Algorithm (using by rank)

class DisjointSetUnion:
    def __init__(self, n):
        # Initialize parent array and rank array
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, u):
        # Find with path compression
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]
    
    def union(self, u, v):
        # Union by rank
        rootU = self.find(u)  # Find root of u
        rootV = self.find(v)  # Find root of v
        
        if rootU != rootV:
            # Attach smaller rank tree under root of higher rank tree
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1

def kruskal(n, edges):
    dsu = DisjointSetUnion(n)
    mst = []
    
    # Sort edges by weight
    edges.sort(key=lambda edge: edge[2])
    
    # Process edges in sorted order
    for u, v, weight in edges:
        # If u and v are in different sets, include this edge in MST
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst.append((u, v, weight))
    
    return mst

# Example usage
n = 5
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst = kruskal(n, edges)
print("Edges in MST:", mst)



# Kruskal's Algorithm (using by size)

class DisjointSetUnion:
    def __init__(self, n):
        # Initialize parent array where each node is its own parent
        self.parent = list(range(n))
        # Initialize sizes of each set to 1
        self.size = [1] * n  
    
    def find(self, u):
        # Find with path compression
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]
    
    def union(self, u, v):
        # Union by size
        rootU = self.find(u)  # Find root of u
        rootV = self.find(v)  # Find root of v
        
        if rootU != rootV:
            # Attach smaller tree under root of larger tree
            if self.size[rootU] > self.size[rootV]:
                self.parent[rootV] = rootU
                self.size[rootU] += self.size[rootV]
            else:
                self.parent[rootU] = rootV
                self.size[rootV] += self.size[rootU]

def kruskal(n, edges):
    dsu = DisjointSetUnion(n)
    mst = []
    
    # Sort edges by weight
    edges.sort(key=lambda edge: edge[2])
    
    # Process edges in sorted order
    for u, v, weight in edges:
        # If u and v are in different sets, include this edge in MST
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst.append((u, v, weight))
    
    return mst

# Example usage
n = 5
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst = kruskal(n, edges)
print("Edges in MST:", mst)



# Time Complexity: O(ElogE), where E is the number of edges.
# Space Complexity: O(E+V) for the parent and rank arrays, and the list of edges.