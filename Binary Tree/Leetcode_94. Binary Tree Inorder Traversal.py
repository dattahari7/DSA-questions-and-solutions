# 94. Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursive Solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Helper function to perform in-order traversal
        def inOrder(root, res):
            if not root:
                return  # Base case: if the node is None, return
            inOrder(root.left, res)  # Recur on the left subtree
            res.append(root.val)  # Visit the root node
            inOrder(root.right, res)  # Recur on the right subtree
        
        res = []  # Initialize an empty list to store the traversal result
        inOrder(root, res)  # Call the helper function to start in-order traversal
        return res  # Return the result list containing in-order traversal values

# Time Complexity: O(n)
# Space Complexity: O(n) Including stack space for recursion
    

# Iterative Solution(using stack)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node = root  # Start with the root node
        stack = deque()  # Initialize a stack to manage traversal
        res = []  # Initialize an empty list to store the traversal result

        # Continue the loop until there are no nodes to process
        while stack or node:
            # Traverse the left subtree
            while node:
                stack.append(node)  # Push the current node onto the stack
                node = node.left  # Move to the left child
            
            # Process the node at the top of the stack
            node = stack.pop()  # Pop the top node from the stack
            res.append(node.val)  # Visit the node and add its value to the result list
            
            # Traverse the right subtree
            node = node.right  # Move to the right child
        
        return res  # Return the final list containing in-order traversal


# Time Complexity: O(n)
# Space Complexity: O(n)
    