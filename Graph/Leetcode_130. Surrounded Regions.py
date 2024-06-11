# 130. Surrounded Regions

# Optimal Solution (using BFS)

from collections import deque
from typing import List

class Solution:
    def bfs(self, row, col, board, visited, directions):
        # Initialize the queue with the starting cell (row, col)
        queue = deque([(row, col)])
        # Mark the starting cell as visited
        visited[row][col] = 1
        
        # Process the queue until it is empty
        while queue:
            # Dequeue the front element
            r, c = queue.popleft()
            # Explore all four possible directions
            for dir_x, dir_y in directions:
                # Calculate the new coordinates after moving in the current direction
                dx, dy = r + dir_x, c + dir_y
                # Check if the new coordinates are within the board boundaries,
                # if the new cell is not visited, and if the new cell contains an 'O'
                if 0 <= dx < len(board) and 0 <= dy < len(board[0]) and not visited[dx][dy] and board[dx][dy] == 'O':
                    # Mark the new cell as visited
                    visited[dx][dy] = 1
                    # Enqueue the new cell
                    queue.append((dx, dy))

    def solve(self, board: List[List[str]]) -> None:
        # If the board is empty, return immediately
        if not board:
            return

        # Get the number of rows (n) and columns (m) in the board
        n = len(board)
        m = len(board[0])
        # Initialize the visited matrix with zeros (0 means unvisited)
        visited = [[0 for _ in range(m)] for _ in range(n)]
        # Define possible directions for movement: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Mark the boundary 'O's and their connected 'O's using BFS
        for j in range(m):
            # Check the first row, column by column
            if not visited[0][j] and board[0][j] == 'O':
                self.bfs(0, j, board, visited, directions)
            # Check the last row, column by column
            if not visited[n-1][j] and board[n-1][j] == 'O':
                self.bfs(n-1, j, board, visited, directions)

        for i in range(n):
            # Check the first column, row by row
            if not visited[i][0] and board[i][0] == 'O':
                self.bfs(i, 0, board, visited, directions)
            # Check the last column, row by row
            if not visited[i][m-1] and board[i][m-1] == 'O':
                self.bfs(i, m-1, board, visited, directions)

        # Flip all 'O's that are not marked as visited to 'X'
        for i in range(n):
            for j in range(m):
                # If a cell contains 'O' and it is not visited, change it to 'X'
                if not visited[i][j] and board[i][j] == 'O':
                    board[i][j] = 'X'


# Time Complexity: O(N * M)
# Space Complexity: O(N * M)


# Optimal Solution (using DFS)
from typing import List

class Solution:
    def dfs(self, row, col, board, visited, directions):
        # Mark the current cell as visited
        visited[row][col] = 1
        # Explore all four possible directions
        for dir_x, dir_y in directions:
            # Calculate the new coordinates after moving in the current direction
            dx, dy = row + dir_x, col + dir_y
            # Check if the new coordinates are within the board boundaries,
            # if the new cell is not visited, and if the new cell contains an 'O'
            if 0 <= dx < len(board) and 0 <= dy < len(board[0]) and visited[dx][dy] == 0 and board[dx][dy] == 'O':
                # Recursively perform DFS on the new cell
                self.dfs(dx, dy, board, visited, directions)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Get the number of rows (n) and columns (m) in the board
        n = len(board)
        m = len(board[0])
        # Initialize the visited matrix with zeros (0 means unvisited)
        visited = [[0 for _ in range(m)] for _ in range(n)]
        # Define possible directions for movement: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Perform DFS for 'O's on the first and last row
        for j in range(m):
            # Check the first row, column by column
            if visited[0][j] == 0 and board[0][j] == 'O':
                self.dfs(0, j, board, visited, directions)
            # Check the last row, column by column
            if visited[n-1][j] == 0 and board[n-1][j] == 'O':
                self.dfs(n-1, j, board, visited, directions)

        # Perform DFS for 'O's on the first and last column
        for i in range(n):
            # Check the first column, row by row
            if visited[i][0] == 0 and board[i][0] == 'O':
                self.dfs(i, 0, board, visited, directions)
            # Check the last column, row by row
            if visited[i][m-1] == 0 and board[i][m-1] == 'O':
                self.dfs(i, m-1, board, visited, directions)

        # Iterate through the entire board to convert unvisited 'O's to 'X's
        for i in range(n):
            for j in range(m):
                # If a cell contains 'O' and it is not visited, change it to 'X'
                if visited[i][j] == 0 and board[i][j] == 'O':
                    board[i][j] = 'X'

# Time Complexity: O(N * M)
# Space Complexity: O(N * M)