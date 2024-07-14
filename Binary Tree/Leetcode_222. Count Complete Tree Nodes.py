# 222. Count Complete Tree Nodes

# BruteForce Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Initialize the count as a list to keep track of the node count
        count = [0]
        
        # Define the inorder traversal function
        def inorder(node, count):
            # If the node is None, return
            if not node:
                return
            # Increment the count for the current node
            count[0] += 1
            # Recursively call inorder on the left child
            inorder(node.left, count)
            # Recursively call inorder on the right child
            inorder(node.right, count)
        
        # Call the inorder function starting from the root
        inorder(root, count)
        
        # Return the total count of nodes
        return count[0]


# Time Complexity: O(N)
# Space Complexity: O(N)


# Optimal Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Base case: if the tree is empty
        if not root:
            return 0
        
        # Find the height of the leftmost path
        lh = self.findLeftHeight(root)
        # Find the height of the rightmost path
        rh = self.findRightHeight(root)

        # If the left and right heights are the same, it's a perfect binary tree
        if lh == rh:
            return (1 << lh) - 1
        
        # Otherwise, recursively count nodes in left and right subtrees
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def findLeftHeight(self, node):
        # Initialize height to 0
        h = 0
        # Traverse down the left subtree
        while node:
            h += 1
            node = node.left
        return h

    def findRightHeight(self, node):
        # Initialize height to 0
        h = 0
        # Traverse down the right subtree
        while node:
            h += 1
            node = node.right
        return h


# Time Complexity: O(log N * log N)
# Space Complexity: O(N)