# Number Of Islands-II

# Optimal Solution (using union-find)

from typing import List

class DisjointSetUnion:
    def __init__(self, n):
        # Initialize the parent array, where each element is its own parent
        self.parent = list(range(n + 1))
        # Initialize the size array to keep track of the size of each set
        self.size = [1] * (n + 1)
        
    def find(self, u):
        # Find with path compression
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
        
    def union(self, u, v):
        # Union by size
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.size[root_u] < self.size[root_v]:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]

class Solution:
    def numOfIslands(self, rows: int, cols: int, operators: List[List[int]]) -> List[int]:
        # Initialize the Disjoint Set Union with a size of rows * cols
        dsu = DisjointSetUnion(rows * cols)
        # Create a visited matrix to keep track of visited cells
        vis = [[0] * cols for _ in range(rows)]
        # List to store the results
        res = []
        # Initialize the count of islands
        count = 0
        
        # Iterate over each operator (which represents an add land operation)
        for row, col in operators:
            # If the cell is already visited, simply append the current count and continue
            if vis[row][col] == 1:
                res.append(count)
                continue
            
            # Mark the cell as visited
            vis[row][col] = 1
            # Increment the island count
            count += 1
            
            # Possible directions to move (up, down, left, right)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            # Check all four possible directions
            for dr, dc in directions:
                adj_row, adj_col = row + dr, col + dc
                
                # If the adjacent cell is within bounds and is visited
                if 0 <= adj_row < rows and 0 <= adj_col < cols and vis[adj_row][adj_col] == 1:
                    # Convert 2D coordinates to 1D
                    node_no = row * cols + col
                    adj_node_no = adj_row * cols + adj_col
                    
                    # If the current cell and the adjacent cell belong to different sets, union them
                    if dsu.find(node_no) != dsu.find(adj_node_no):
                        count -= 1
                        dsu.union(node_no, adj_node_no)
                        
            # Append the current island count to the result list
            res.append(count)
        
        return res

