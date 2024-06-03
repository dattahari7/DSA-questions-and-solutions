# 700. Search in a Binary Search Tree

# Optimal Solution

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If root is None, return None
        if not root:
            return None
        # Traverse the tree while the current node is not None and its value is not equal to the target value
        while root is not None and root.val != val:
            # Move to the left subtree if the target value is less than the current node's value
            root = root.left if val < root.val else root.right
        # Return the node with the target value or None if not found
        return root


# Time Complexity: O(log(n))
# Space Complexity: O(1)