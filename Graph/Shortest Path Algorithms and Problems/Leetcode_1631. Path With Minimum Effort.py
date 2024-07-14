# 1631. Path With Minimum Effort

# Optimal Solution (using Dijkstra's algorithm)
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Get the dimensions of the grid
        n, m = len(heights), len(heights[0])
        
        # Initialize distance array with infinity
        dist = [[float('inf') for _ in range(m)] for _ in range(n)]
        dist[0][0] = 0
        
        # Min-heap priority queue to store (effort, row, col)
        pq = [(0, 0, 0)]
        
        # Directions array for the 4 possible movements
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while pq:
            # Pop the smallest effort from the priority queue
            effort, row, col = heapq.heappop(pq)

            # If the destination is reached, return the effort
            if row == n - 1 and col == m - 1:
                return effort
            
            # Explore all 4 possible directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # Check if the new position is within bounds
                if 0 <= new_row < n and 0 <= new_col < m:
                    # Calculate the effort to move to the new cell
                    new_diff = abs(heights[row][col] - heights[new_row][new_col])
                    new_effort = max(effort, new_diff)
                    
                    # Update the distance if a smaller effort is found
                    if new_effort < dist[new_row][new_col]:
                        dist[new_row][new_col] = new_effort
                        heapq.heappush(pq, (new_effort, new_row, new_col))

        # Return 0 if no path is found (should not happen)
        return 0


# Time Complexity: O(N * M log(N * M)) { N*M are the total cells, for each of which we also check 4 adjacent nodes for the minimum effort and additional log(N*M) for insertion-deletion operations in a priority queue } 
# Space Complexity: O(N * M) { Distance matrix containing N*M cells + priority queue in the worst case containing all the nodes ( N*M) }.