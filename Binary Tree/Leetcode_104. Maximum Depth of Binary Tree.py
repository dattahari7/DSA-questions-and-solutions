# 104. Maximum Depth of Binary Tree

# Optimal Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # Base case: if the node is None, the depth is 0
        
        # Recursively find the depth of the left subtree
        left_height = self.maxDepth(root.left)
        
        # Recursively find the depth of the right subtree
        right_height = self.maxDepth(root.right)
        
        # Calculate the maximum depth by taking the maximum of the left and right subtree depths and adding 1 for the current node
        return 1 + max(left_height, right_height)

# Time Complexity: O(n)
# Space Complexity: O(n) used recursive stack space
