# 1319. Number of Operations to Make Network Connected

# Optimal Solution 

class DisjointSetUnion:
    def __init__(self, n):
        # Initialize parent array where each node is its own parent
        self.parent = list(range(n))
        # Initialize sizes of each set to 1
        self.size = [1] * n

    def find(self, u):
        # Find with path compression
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        # Union by size
        root_u = self.find(u)  # Find root of u
        root_v = self.find(v)  # Find root of v
        
        if root_u != root_v:
            # Attach smaller tree under root of larger tree
            if self.size[root_u] < self.size[root_v]:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]
    
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        dsu = DisjointSetUnion(n)
        extraCount = 0
        
        for u, v in connections:
            # Check if u and v are already connected
            if dsu.find(u) == dsu.find(v):
                extraCount += 1  # Count extra cables
            else:
                dsu.union(u, v)  # Union the components
            
        count = 0
        for i in range(n):
            if dsu.find(i) == i:  # Check for unique parents
                count += 1  # Count of disconnected components
        
        ans = count - 1  # Number of edges needed to connect all components
        if extraCount >= ans:
            return ans  # Return the number of edges needed if enough extra cables
        else:
            return -1  # Return -1 if not enough extra cables
        
# Time Complexity: O(E*4α)+O(N*4α) 4α is for the disjoint set operation we have used and this term is so small that it can be considered constant.
# Space Complexity: O(2N)