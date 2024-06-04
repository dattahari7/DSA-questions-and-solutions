# 542. 01 Matrix

# Optimal Solution

from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Initialize the result matrix with infinity values
        result = [[float("inf") for _ in range(len(mat[0]))] for _ in range(len(mat))]
        # Initialize the visited matrix with zeros (unvisited)
        visited = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]

        # Initialize a queue to perform BFS
        que = deque()

        # Add all the cells with 0s to the queue and mark them as visited
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if (mat[i][j] == 0):
                    que.append((i, j, 0))
                    visited[i][j] = 1

        # Define possible directions for movement (right, left, down, up)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Perform BFS
        while que:
            row, col, steps = que.popleft()
            # Update the result matrix with the number of steps
            result[row][col] = steps
            # Iterate through all possible directions
            for dir_x, dir_y in directions:
                # Calculate the new coordinates
                dx, dy = row + dir_x, col + dir_y
                # If the new coordinates are within bounds and the cell is not visited
                if 0 <= dx < len(mat) and 0 <= dy < len(mat[0]) and visited[dx][dy] == 0:
                    visited[dx][dy] = 1
                    que.append((dx, dy, steps + 1))

        return result

# Time Complexity: O(N * M)
# Space Complexity: O(N * M)
    
