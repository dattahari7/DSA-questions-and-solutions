# 235. Lowest Common Ancestor of a Binary Search Tree

# BruteForce Solution

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Helper function to find the lowest common ancestor
        def LCA(root, p, q):
            # Base case: if the current node is None or matches p or q
            if not root or root == p or root == q:
                return root

            # Recursively search for LCA in the left subtree
            left_node = LCA(root.left, p, q)

            # Recursively search for LCA in the right subtree
            right_node = LCA(root.right, p, q)

            # If neither left nor right subtree contains p or q, return None
            if not left_node:
                return right_node

            # If only the left subtree contains p or q, return left_node
            elif not right_node:
                return left_node

            # If both subtrees contain one of p or q each, return the current node
            else:
                return root

        # Call the helper function starting with the root
        return LCA(root, p, q)

# Time Complexity: O(n)
# Space Complexity: O(n)
    

# Optimal Solution
    
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Iterate through the tree starting from the root
        while root:
            # If both p and q are greater than root, LCA is in the right subtree
            if p.val > root.val and q.val > root.val:
                root = root.right
            # If both p and q are less than root, LCA is in the left subtree
            elif p.val < root.val and q.val < root.val:
                root = root.left
            # If p and q are on different sides of root, or one of them is the root, we've found the LCA
            else:
                return root


# Time Complexity: O(n)
# Space Complexity: O(1)