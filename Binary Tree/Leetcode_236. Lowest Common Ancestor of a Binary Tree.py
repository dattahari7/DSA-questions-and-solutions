# 236. Lowest Common Ancestor of a Binary Tree

# Optimal Solution

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if root is None or root is one of the nodes (p or q)
        if not root or p == root or q == root:
            return root

        # Recur for the left subtree
        left_node = self.lowestCommonAncestor(root.left, p, q)
        # Recur for the right subtree
        right_node = self.lowestCommonAncestor(root.right, p, q)

        # If left_node is None, return right_node
        if not left_node:
            return right_node
        # If right_node is None, return left_node
        elif not right_node:
            return left_node
        # If both left_node and right_node are not None, return root
        else:
            return root

# Time Complexity: O(n)
# Space Complexity: O(n) auxilary space