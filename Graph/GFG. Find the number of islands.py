# Find the number of islands

# Optimal Solution

from collections import deque
class Solution:
    def bfs(self, row, col, grid, vis):
        # Mark the starting cell as visited
        vis[row][col] = 1
        # Initialize the queue with the starting cell
        que = deque([(row, col)])
        
        while que:
            r, c = que.popleft()
            
            # Explore all 8 possible directions (including diagonals)
            for dir_x in range(-1, 2):
                for dir_y in range(-1, 2):
                    # Calculate the new coordinates
                    dx, dy = r + dir_x, c + dir_y
                    # Check if the new coordinates are within bounds, unvisited, and land (1)
                    if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and vis[dx][dy] == 0 and grid[dx][dy] == 1:
                        # Mark the new cell as visited and add it to the queue
                        vis[dx][dy] = 1
                        que.append((dx, dy))
        
    def numIslands(self, grid):
        # Get the number of rows
        n = len(grid)
        # Get the number of columns
        m = len(grid[0])
        # Initialize the visited matrix with zeros
        vis = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        islands_count = 0
        
        # Iterate over each cell in the grid
        for i in range(n):
            for j in range(m):
                # If the cell is unvisited and is land (1), perform BFS
                if vis[i][j] == 0 and grid[i][j] == 1:
                    islands_count += 1
                    self.bfs(i, j, grid, vis)
                    
        return islands_count


# Time Complexity: O(N^2 + N*M*9)
# Space Complexity: O(N^2)