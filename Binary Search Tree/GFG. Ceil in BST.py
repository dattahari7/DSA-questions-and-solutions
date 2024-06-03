# Ceil in BST

# Optimal Solution

class Solution:
    def findCeil(self, root, inp):
        # Initialize the ceil value to -1 (indicating no ceil found yet)
        ceil = -1 
        # Traverse the tree while the current node is not None
        while root:
            # If the current node's key is equal to the input, return the current key as the ceil
            if root.key == inp:
                ceil = root.key
                return ceil
            # If the input is greater than the current key, move to the right subtree
            if inp > root.key:
                root = root.right
            # If the input is less than the current key, update the ceil and move to the left subtree
            else:
                ceil = root.key
                root = root.left
        # Return the ceil value after traversing the tree
        return ceil


# Time Complexity: O(log(n))
# Space Complexity: O(1)
