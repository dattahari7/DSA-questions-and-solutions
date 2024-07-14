# 947. Most Stones Removed with Same Row or Column

# Optimal Solution (using union find)

class DisjointSetUnion:
    def __init__(self, n):
        # Initialize parent array where each node is its own parent initially
        self.parent = list(range(n + 1))
        # Initialize sizes of each set to 1
        self.size = [1] * (n + 1)
    
    def find(self, u):
        # Path compression: makes the tree flat
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        # Union by size: attach smaller tree under root of larger tree
        root_u = self.find(u)  # Find root of u
        root_v = self.find(v)  # Find root of v
        if root_u != root_v:  # Only union if they are in different sets
            if self.size[root_u] < self.size[root_v]:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        max_row = max_col = 0
        # Determine the maximum row and column values
        for i in range(n):
            max_row = max(max_row, stones[i][0])
            max_col = max(max_col, stones[i][1])
        
        # Initialize DisjointSetUnion with size based on the maximum row and column values
        dsu = DisjointSetUnion(max_row + max_col + 1)
        stone_nodes = {}
        for i in range(n):
            node_row = stones[i][0]
            node_col = stones[i][1] + max_row + 1  # Offset column index to avoid collision with row index
            dsu.union(node_row, node_col)  # Union row and column indices
            stone_nodes[node_row] = 1  # Mark row as having a stone
            stone_nodes[node_col] = 1  # Mark column as having a stone

        count = 0
        for key in stone_nodes:
            if dsu.find(key) == key:  # Count unique roots
                count += 1
        
        return n - count  # The number of moves is the total stones minus the number of unique roots


# Time Complexity: O(N), where N = total no. of stones. Here we have just traversed the given stones array several times. And inside those loops, every operation is apparently taking constant time. So, the time complexity is only the time of traversal of the array.

# Space Complexity: O(2* (max row index + max column index)) for the parent and size array inside the Disjoint Set data structure.