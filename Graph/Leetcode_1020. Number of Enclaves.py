# 1020. Number of Enclaves

# Optimal Solution (using BFS)

from collections import deque
from typing import List

class Solution:
    def bfs(self, row, col, grid, vis, directions):
        # Initialize the queue with the starting cell
        que = deque([(row, col)])
        # Mark the starting cell as visited
        vis[row][col] = 1
        while que:
            # Pop the first cell in the queue
            r, c = que.popleft()
            # Explore all four possible directions
            for dir_x, dir_y in directions:
                # Calculate the new coordinates
                dx, dy = r + dir_x, c + dir_y
                # Check if the new coordinates are within bounds and the cell is unvisited and is land (1)
                if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and vis[dx][dy] == 0 and grid[dx][dy] == 1:
                    # Add the new cell to the queue and mark it as visited
                    que.append((dx, dy))
                    vis[dx][dy] = 1

    def numEnclaves(self, grid: List[List[int]]) -> int:
        # Initialize the visited matrix with zeros
        vis = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        # Define possible directions for movement: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        n = len(grid)  # Number of rows
        m = len(grid[0])  # Number of columns

        # Perform BFS for all boundary cells
        for j in range(m):
            # Check the first row
            if vis[0][j] == 0 and grid[0][j] == 1:
                self.bfs(0, j, grid, vis, directions)
            # Check the last row
            if vis[n-1][j] == 0 and grid[n-1][j] == 1:
                self.bfs(n-1, j, grid, vis, directions)

        for i in range(n):
            # Check the first column
            if vis[i][0] == 0 and grid[i][0] == 1:
                self.bfs(i, 0, grid, vis, directions)
            # Check the last column
            if vis[i][m-1] == 0 and grid[i][m-1] == 1:
                self.bfs(i, m-1, grid, vis, directions)

        # Count the number of land cells not visited
        land_count = 0
        for i in range(n):
            for j in range(m):
                if vis[i][j] == 0 and grid[i][j] == 1:
                    land_count += 1

        return land_count


# Time Complexity: O(N * M)
# Space Complexity: O(N * M)


# Optimal Solution (using DFS)

class Solution:
    def dfs(self, row, col, grid, vis, directions):
        # Mark the current cell as visited
        vis[row][col] = 1
        # Explore all four possible directions
        for dir_x, dir_y in directions:
            # Calculate the new coordinates
            dx, dy = row + dir_x, col + dir_y
            # Check if the new coordinates are within bounds and the cell is unvisited and is land (1)
            if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and vis[dx][dy] == 0 and grid[dx][dy] == 1:
                # Perform DFS on the new cell
                self.dfs(dx, dy, grid, vis, directions)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        # Initialize the visited matrix with zeros
        vis = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        # Define possible directions for movement: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        n = len(grid)  # Number of rows
        m = len(grid[0])  # Number of columns

        # Perform DFS for all boundary cells
        for j in range(m):
            # Check the first row
            if vis[0][j] == 0 and grid[0][j] == 1:
                self.dfs(0, j, grid, vis, directions)
            # Check the last row
            if vis[n-1][j] == 0 and grid[n-1][j] == 1:
                self.dfs(n-1, j, grid, vis, directions)

        for i in range(n):
            # Check the first column
            if vis[i][0] == 0 and grid[i][0] == 1:
                self.dfs(i, 0, grid, vis, directions)
            # Check the last column
            if vis[i][m-1] == 0 and grid[i][m-1] == 1:
                self.dfs(i, m-1, grid, vis, directions)

        # Count the number of land cells not visited
        land_count = 0
        for i in range(n):
            for j in range(m):
                if vis[i][j] == 0 and grid[i][j] == 1:
                    land_count += 1

        return land_count

# Time Complexity: O(N * M)
# Space Complexity: O(N * M)
    

