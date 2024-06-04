# 733. Flood Fill

# Optimal Solution (with DFS algorithm)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Create a copy of the image to avoid modifying the original one
        result = [row[:] for row in image]
        # Store the initial color of the starting pixel
        iniColor = image[sr][sc]
        # Define the possible directions for movement (right, left, down, up)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # Start the depth-first search from the starting pixel
        self.dfs(image, sr, sc, directions, color, iniColor, result)
        return result

    def dfs(self, image, row, col, directions, newColor, iniColor, result):
        # Fill the current pixel with the new color
        result[row][col] = newColor
        # Iterate through all possible directions
        for dir_x, dir_y in directions:
            # Calculate the new coordinates
            dx, dy = row + dir_x, col + dir_y
            # Check if the new coordinates are within the image bounds
            # and if the color at the new coordinates is the initial color
            # and not yet filled with the new color
            if 0 <= dx < len(image) and 0 <= dy < len(image[0]) and result[dx][dy] == iniColor and result[dx][dy] != newColor:
                # Recursively apply DFS to the neighboring pixel
                self.dfs(image, dx, dy, directions, newColor, iniColor, result)

# Time Complexity: O(N * N)
# Space Complexity: O(N)

# Optimal Solution (with BFS algorithm)
                
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Create a copy of the image to avoid modifying the original one
        result = [row[:] for row in image]
        # Store the initial color of the starting pixel
        iniColor = image[sr][sc]
        # If the initial color is the same as the new color, return the original image
        if iniColor == color:
            return result
        # Define the possible directions for movement (right, left, down, up)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # Use a queue for breadth-first search, starting with the given pixel
        que = deque([(sr, sc)])
        while que:
            # Get the current pixel coordinates from the queue
            row, col = que.popleft()
            # Fill the current pixel with the new color
            result[row][col] = color
            # Iterate through all possible directions
            for dir_x, dir_y in directions:
                # Calculate the new coordinates
                dx, dy = row + dir_x, col + dir_y
                # Check if the new coordinates are within the image bounds
                # and if the color at the new coordinates is the initial color
                # and not yet filled with the new color
                if 0 <= dx < len(image) and 0 <= dy < len(image[0]) and result[dx][dy] == iniColor and result[dx][dy] != color:
                    # Add the new coordinates to the queue
                    que.append((dx, dy))
        return result


# Time Complexity: O(N * N)
# Space Complexity: O(N)