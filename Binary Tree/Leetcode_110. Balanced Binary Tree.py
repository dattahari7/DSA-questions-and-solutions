# 110. Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function to find the height of a subtree and check if it's balanced
        def findHeight(root):
            if not root:
                return 0  # Base case: if the node is None, the height is 0
            
            leftHeight = findHeight(root.left)  # Recursively find the height of the left subtree
            if leftHeight == -1:
                return -1  # If the left subtree is unbalanced, propagate the -1 upwards
            
            rightHeight = findHeight(root.right)  # Recursively find the height of the right subtree
            if rightHeight == -1:
                return -1  # If the right subtree is unbalanced, propagate the -1 upwards
            
            # Check if the current node's subtrees differ in height by more than 1
            if abs(leftHeight - rightHeight) > 1:
                return -1  # If they do, the current subtree is unbalanced
            
            return max(leftHeight, rightHeight) + 1  # Return the height of the current subtree
        
        return findHeight(root) != -1  # The tree is balanced if findHeight doesn't return -1

# Time Complexity: O(n)
# Space Complexity: O(n)