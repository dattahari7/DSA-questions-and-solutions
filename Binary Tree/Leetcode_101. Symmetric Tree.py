# 101. Symmetric Tree

# Optimal Solution

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # If the root is None, the tree is symmetric
        if root is None:
            return True
        
        # Helper function to check symmetry between two subtrees
        def helper(left_node, right_node):
            # If either of the nodes is None, check if both are None (symmetry)
            if left_node is None or right_node is None:
                return left_node == right_node
            # If the values of the nodes do not match, it's not symmetric
            if left_node.val != right_node.val:
                return False
            # Check the symmetry of left and right subtrees recursively
            return helper(left_node.left, right_node.right) and helper(left_node.right, right_node.left)
        
        # Start the helper function with the left and right children of the root
        return helper(root.left, root.right)


# Time Complexity: O(n)
# Space Complexity: O(1)