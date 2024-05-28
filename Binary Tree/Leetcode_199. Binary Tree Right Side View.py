# 199. Binary Tree Right Side View

# Optimal Solution

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Helper function to perform a depth-first traversal
        def helper(root, level):
            if not root:
                return
            # If we are visiting a new level for the first time, add the node's value to the result
            if level == len(res):
                res.append(root.val)
            # First, try to visit the right child to ensure the rightmost node is seen
            helper(root.right, level + 1)
            # Then, visit the left child
            helper(root.left, level + 1)

        # Initialize the result list to store the right side view
        res = []
        # Start the helper function with the root node at level 0
        helper(root, 0)
        # Return the final right side view
        return res


# Time Complexity: O(n)
# Space Complexity: O(H) here H is height of tree
