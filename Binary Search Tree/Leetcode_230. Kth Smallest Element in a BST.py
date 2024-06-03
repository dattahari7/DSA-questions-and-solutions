# 230. Kth Smallest Element in a BST

# BruteForce Solution

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Helper function for in-order traversal of the tree
        def inOrder(root):
            if not root:
                return
            # Traverse the left subtree
            inOrder(root.left)
            # Append the current node's value to the result list
            res.append(root.val)
            # Traverse the right subtree
            inOrder(root.right)
        
        res = []
        # If the tree is empty, return None
        if not root:
            return None
            
        # Perform in-order traversal to collect node values in sorted order
        inOrder(root)
        # Return the k-th smallest element (1-based index)
        return res[k-1]

# Time Complexity: O(n)
# Space Complexity: O(n)
    

# Optimal Solution
    
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize a counter for the number of visited nodes
        n = 0
        # Stack to perform iterative in-order traversal
        stack = []
        # Start with the root node
        cur = root

        # Iterate until we have nodes to process
        while cur or stack:
            # Traverse to the leftmost node
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # Process the node on top of the stack
            cur = stack.pop()
            # Increment the count of visited nodes
            n += 1
            # If we've reached the k-th smallest node, return its value
            if n == k:
                return cur.val
            # Move to the right subtree
            cur = cur.right


# Time Complexity: O(H) here H is height of BST
# Space Complexity: O(1)