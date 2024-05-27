# 100. Same Tree

# Optimal Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: if both nodes are None, they are the same
        if not p and not q:
            return True
        # If one of the nodes is None while the other is not, they are not the same
        if not p or not q:
            return False

        # Check if the values of the current nodes are equal
        # and recursively check if their left and right subtrees are the same
        return (p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

# Time Complexity: O(m + n)
# Space Complexity: O(1)

