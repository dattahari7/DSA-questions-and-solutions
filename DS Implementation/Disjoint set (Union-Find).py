# Disjoint set (Union-Find)

# Optimal Solution (using by Rank)

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Example usage:
ds = DisjointSet(6)
ds.union(1, 2)
ds.union(3, 4)
print(ds.find(2))  # Output should be 1 or 2 depending on path compression
print(ds.find(3))  # Output should be 3 or 4 depending on path compression
ds.union(2, 4)
print(ds.find(4))  # Output should be 1, 2, 3, or 4 depending on path compression


# Optimal Solution (using by size)

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            # Union by size
            if self.size[root_u] < self.size[root_v]:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]

# Example usage:
ds = DisjointSet(6)
ds.union(1, 2)
ds.union(3, 4)
print(ds.find(2))  # Output should be 1 or 2 depending on path compression
print(ds.find(3))  # Output should be 3 or 4 depending on path compression
ds.union(2, 4)
print(ds.find(4))  # Output should be 1, 2, 3, or 4 depending on path compression


# Time Complexity: O(4*alpha) ~ O(1)
# Space Complexity: O(n)


# test code

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

# Example usage:
ds = DisjointSet(6)
ds.union(1, 2)
ds.union(3, 4)
print(ds.find(2))  # Output should be 1 or 2 depending on path compression
print(ds.find(3))  # Output should be 3 or 4 depending on path compression
ds.union(2, 4)
print(ds.find(4))  # Output should be 1, 2, 3, or 4 depending on path compression