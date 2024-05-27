# 144. Binary Tree Preorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursive Solution

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Helper function to perform pre-order traversal
        def preOrder(root, res):
            if not root:
                return  # Base case: if the node is None, return
            res.append(root.val)  # Visit the root node and add its value to the result list
            preOrder(root.left, res)  # Recur on the left subtree
            preOrder(root.right, res)  # Recur on the right subtree
        
        res = []  # Initialize an empty list to store the traversal result
        preOrder(root, res)  # Call the helper function to start pre-order traversal
        return res  # Return the result list containing pre-order traversal values

# Time Complexity: O(n)
# Space Complexity: O(n) Including stack space for recursion



# Iterative solution
    
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # Initialize an empty list to store the traversal result
        if not root:
            return res  # If the tree is empty, return the empty result list
        
        stack = deque()  # Initialize a stack for iterative traversal
        stack.append(root)  # Start with the root node
        
        while stack:
            root = stack.pop()  # Pop the top node from the stack
            res.append(root.val)  # Visit the node and add its value to the result list
            
            if root.right:  # If the right child exists, push it onto the stack
                stack.append(root.right)
            if root.left:  # If the left child exists, push it onto the stack
                stack.append(root.left)
        
        return res  # Return the final list containing pre-order traversal

# Time Complexity: O(n)
# Space Complexity: O(n) used stack