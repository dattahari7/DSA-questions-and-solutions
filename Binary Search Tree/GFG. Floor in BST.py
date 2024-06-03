# Floor in BST

# Optimal Solution

class Solution:
    def floor(self, root, x):
        # Initialize the floor value to -1 (indicating no floor found yet)
        floor = -1
        # Traverse the tree while the current node is not None
        while root:
            # If the current node's data is equal to the input, return the current data as the floor
            if root.data == x:
                floor = root.data
                return floor
            # If the input is less than the current data, move to the left subtree
            if x < root.data:
                root = root.left
            # If the input is greater than the current data, update the floor and move to the right subtree
            else:
                floor = root.data
                root = root.right
        # Return the floor value after traversing the tree
        return floor


# Time Complexity: O(log(n))
# Space Complexity: O(1)