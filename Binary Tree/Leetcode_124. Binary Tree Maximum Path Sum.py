# 124. Binary Tree Maximum Path Sum

# BruteForce Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # To keep track of the maximum path sum
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # Get the path sum for the left and right subtree
            left = explorePaths(node.left)
            right = explorePaths(node.right)
            
            # Update the maximum path sum for paths passing through this node
            self.max_sum = max(self.max_sum, left + node.val, right + node.val, left + right + node.val, node.val)
            
            # Explore paths starting from the left and right children
            dfs(node.left)
            dfs(node.right)
        
        def explorePaths(node):
            if not node:
                return 0
            
            # Calculate maximum path sum with the current node as the highest point
            left = explorePaths(node.left)
            right = explorePaths(node.right)
            
            # Calculate the maximum path sum considering current node
            current_sum = max(left + node.val, right + node.val, left + right + node.val, node.val)
            
            # Update the global maximum path sum if the current path sum is higher
            self.max_sum = max(self.max_sum, current_sum)
            
            # Return the maximum gain the node and one of its subtrees can contribute to the path
            return max(left + node.val, right + node.val, node.val)
        
        # Start DFS from the root to explore all paths
        dfs(root)
        
        return self.max_sum
     
# Time Complexity: O(n*n)
# Space Complexity: O(1) except recursive stack space
    

# Optimal Solution
    
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # To keep track of the maximum path sum
        self.max_sum = float('-inf')
        
        # Helper function to calculate maximum path sum for each node
        def maxPath(node):
            if not node:
                return 0  # Base case: if the node is None, the path sum is 0

            # Recursively find the maximum path sum of the left subtree, ignore negative sums
            left_sum = max(maxPath(node.left), 0)
            # Recursively find the maximum path sum of the right subtree, ignore negative sums
            right_sum = max(maxPath(node.right), 0)
            
            # Update the maximum path sum including the current node
            self.max_sum = max(self.max_sum, left_sum + right_sum + node.val)
            
            # Return the maximum sum path of either left or right subtree including the current node
            return node.val + max(left_sum, right_sum)
        
        maxPath(root)  # Start the recursion from the root
        return self.max_sum  # Return the maximum path sum found



# Time Complexity: O(n)
# Space Complexity: O(1) except recursive stack space
    
