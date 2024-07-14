# 778. Swim in Rising Water

# Optimal Solution (using Dijkstra's algorithm)

import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)  # Get the size of the grid
        pq = [(grid[0][0], 0, 0)]  # Priority queue with the starting point (elevation, row, column)
        visited = set([(0, 0)])  # Set to keep track of visited cells
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Possible movements (right, down, left, up)

        while pq:
            t, r, c = heapq.heappop(pq)  # Pop the cell with the minimum elevation

            # If we reach the bottom-right cell, return the time
            if r == n - 1 and c == n - 1:
                return t
            
            # Explore all possible directions
            for dr, dc in directions:
                adjr, adjc = r + dr, c + dc  # Calculate the coordinates of the adjacent cell
                if 0 <= adjr < n and 0 <= adjc < n and (adjr, adjc) not in visited:  # Check if the cell is within bounds and not visited
                    newTime = max(t, grid[adjr][adjc])  # Calculate the maximum elevation encountered so far
                    visited.add((adjr, adjc))  # Mark the cell as visited
                    heapq.heappush(pq, (newTime, adjr, adjc))  # Push the new cell into the priority queue

        return -1  # In case no path is found (shouldn't happen with valid input)


# Time Complexity: O(N * M log(N * M)) { N*M are the total cells, for each of which we also check 4 adjacent nodes for the minimum time and additional log(N*M) for insertion-deletion operations in a priority queue } 
# Space Complexity: O(N * M) {priority queue in the worst case containing all the nodes ( N*M) }.