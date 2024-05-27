# 543. Diameter of Binary Tree

# BruteForce Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0  # If the tree is empty, the diameter is 0

        # Helper function to compute the height of a subtree
        def height(node):
            if not node:
                return 0  # Base case: if the node is None, the height is 0
            return 1 + max(height(node.left), height(node.right))  # Height of a node is 1 + max of left and right subtree heights

        # Helper function to compute the diameter of a subtree rooted at the given node
        def diameter(node):
            if not node:
                return 0  # Base case: if the node is None, the diameter is 0
            left_height = height(node.left)  # Height of the left subtree
            right_height = height(node.right)  # Height of the right subtree
            return left_height + right_height  # Diameter is the sum of left and right subtree heights

        # Helper function to find the maximum diameter in the tree
        def max_diameter(node):
            if not node:
                return 0  # Base case: if the node is None, the maximum diameter is 0
            # The maximum diameter is the largest of the diameters through the current node, the left subtree, and the right subtree
            return max(diameter(node), max_diameter(node.left), max_diameter(node.right))

        return max_diameter(root)  # Start the recursive function from the root and return the maximum diameter found


# Time Complexity: O(n*n)
# Space Complexity: O(1) expect recursive stack space


# Optimal Solution

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0  # Initialize the maximum diameter to 0

        def findMax(node):
            if not node:
                return 0  # Base case: if the node is None, the height is 0

            # Recursively find the height of the left subtree
            left_height = findMax(node.left)
            
            # Recursively find the height of the right subtree
            right_height = findMax(node.right)

            # Update the maximum diameter if the path through the current node is larger
            self.max_len = max(self.max_len, left_height + right_height)

            # Return the height of the current node
            return max(left_height, right_height) + 1

        findMax(root)  # Start the recursive function from the root
        return self.max_len  # Return the maximum diameter found


# Time Complexity: O(n)
# Space Complexity: O(1) except recursive stack space



