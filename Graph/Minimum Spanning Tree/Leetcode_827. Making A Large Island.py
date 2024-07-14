# 827. Making A Large Island

# Optimal Solution (using union find)

class DisjointSetUnion:
    def __init__(self, n):
        # Initialize parent and size arrays
        # parent[i] points to the parent of i, initially itself
        # size[i] stores the size of the set where i belongs
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, u):
        # Path compression heuristic
        # If u is not its own parent, recursively find the root and compress the path
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        # Union by size heuristic
        # Find the roots of the sets u and v belong to
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            # Attach the smaller tree under the larger tree
            if self.size[root_u] < self.size[root_v]:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]


class Solution:
    def isValid(self, adjr, adjc, n):
        # Check if the cell (adjr, adjc) is within the grid boundaries
        return 0 <= adjr < n and 0 <= adjc < n

    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dsu = DisjointSetUnion(n * n)

        # Union adjacent land cells
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue
                # Directions for exploring adjacent cells (up, down, left, right)
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in directions:
                    adjr, adjc = row + dr, col + dc
                    if self.isValid(adjr, adjc, n) and grid[adjr][adjc] == 1:
                        # Calculate unique node numbers for the disjoint set union
                        curr_node_no = row * n + col
                        adj_node_no = adjr * n + adjc
                        dsu.union(curr_node_no, adj_node_no)

        mx = 0

        # Check for the maximum size of island by flipping one 0 to 1
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    continue
                # Set to keep track of unique connected components
                components = set()
                # Directions for exploring adjacent cells (up, down, left, right)
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in directions:
                    adjr, adjc = row + dr, col + dc
                    if self.isValid(adjr, adjc, n) and grid[adjr][adjc] == 1:
                        adj_node_no = adjr * n + adjc
                        components.add(dsu.find(adj_node_no))
                # Calculate the total size by merging components and adding the flipped cell
                sizeTotal = sum(dsu.size[parent] for parent in components)
                mx = max(mx, sizeTotal + 1)

        # Check if the largest island is the original one without flipping any 0
        for cellNo in range(n * n):
            mx = max(mx, dsu.size[dsu.find(cellNo)])

        return mx


# Time Complexity: O(N2)+O(N2) ~ O(N2) where N = total number of rows of the grid. Inside those nested loops, all the operations are taking apparently constant time. So, O(N2) for the nested loop only, is the time complexity.

# Space Complexity: O(2*N2) where N = the total number of rows of the grid. This is for the two arrays i.e. parent array and size array of size N2 inside the Disjoint set.