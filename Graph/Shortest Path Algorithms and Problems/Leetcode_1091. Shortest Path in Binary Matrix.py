# 1091. Shortest Path in Binary Matrix

# Optimal Solution (using only queue)

from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Get the size of the grid
        n = len(grid)
        
        # If the start or end cell is blocked, return -1 as no path is possible
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        # Directions array representing the 8 possible moves (including diagonals)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Queue to perform BFS, starting with the top-left cell and initial path length of 1
        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        
        # Set to track visited cells
        visited = set((0, 0))
        
        # BFS loop
        while queue:
            # Get the current cell and path length from the queue
            row, col, path_length = queue.popleft()
            
            # If the bottom-right cell is reached, return the path length
            if row == n-1 and col == n-1:
                return path_length
            
            # Explore all 8 possible directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if the new cell is within bounds, not blocked, and not visited
                if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                    # Mark the cell as visited and add it to the queue with the updated path length
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, path_length + 1))
        
        # If the queue is exhausted and the destination is not reached, return -1
        return -1


# Time Complexity: O(M * log N)
# Space Complexity: O(N)