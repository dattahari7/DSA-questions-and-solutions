# 98. Validate Binary Search Tree

# BruteForce Solution

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function to perform in-order traversal and collect node values
        def inOrder(root, result):
            if not root:
                return None
            inOrder(root.left, result)  # Traverse the left subtree
            result.append(root.val)  # Append the current node value
            inOrder(root.right, result)  # Traverse the right subtree
        
        # Helper function to check if the BST is valid using in-order traversal result
        def helper(root, result):
            if not root:
                return None
            inOrder(root, result)  # Populate result with in-order traversal values

            # Check if the in-order traversal result is sorted in strictly increasing order
            for i in range(1, len(result)):
                if result[i-1] >= result[i]:
                    return False  # Return False if any adjacent values are not in order
            return True  # Return True if all values are in order

        result = []
        return helper(root, result)

# Time Complexity: O(n)
# Space Complexity: O(n)


# Optimal solution

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function to validate the BST properties recursively
        def helper(root, minVal, maxVal):
            # If we reach a leaf node, it's a valid subtree
            if not root:
                return True
            # If the current node's value is outside the valid range, return False
            if root.val >= maxVal or root.val <= minVal:
                return False

            # Recursively validate the left and right subtrees
            # For the left subtree, update the maxVal to the current node's value
            # For the right subtree, update the minVal to the current node's value
            return helper(root.left, minVal, root.val) and helper(root.right, root.val, maxVal)
        
        # Initialize the recursion with the full range of valid values
        return helper(root, float("-inf"), float("inf"))


# Time Complexity: O(n)
# Space Complexity: O(1)