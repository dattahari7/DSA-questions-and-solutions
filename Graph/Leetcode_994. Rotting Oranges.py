# 994. Rotting Oranges

# Optimal Solution

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Directions for moving in the grid (left, right, up, down)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Queue to perform BFS and count of fresh oranges
        que = deque()
        fresh_oranges = 0

        # Traverse the grid to initialize the queue with rotten oranges
        # and count the fresh oranges
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    que.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        
        # If there are no fresh oranges, return 0
        if fresh_oranges == 0:
            return 0

        # Initialize the total minutes counter
        total_minTime = 0
        # Perform BFS to rot the fresh oranges
        while que:
            total_minTime += 1
            # Process all rotten oranges at the current time step
            for _ in range(len(que)):
                x, y = que.popleft()
                # Check all 4 possible directions
                for dir_x, dir_y in directions:
                    dx, dy = x + dir_x, y + dir_y
                    # If the adjacent cell contains a fresh orange, rot it
                    if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and grid[dx][dy] != 0 and grid[dx][dy] == 1:
                        grid[dx][dy] = 2
                        fresh_oranges -= 1
                        que.append((dx, dy))
            
        # If there are still fresh oranges, return -1, otherwise Return minutes passed minus one because we increment it one last time after processing
        return -1 if fresh_oranges else total_minTime - 1

# Time Complexity: O(N * N)
# Space Complexity: O(N)
    