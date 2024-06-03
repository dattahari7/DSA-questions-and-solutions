# 701. Insert into a Binary Search Tree

# Optimal Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If the tree is empty, create a new node with the given value and return it
        if not root:
            return TreeNode(val)
        
        # Start traversing the tree from the root
        curr = root
        while True:
            # If the current node's value is less than or equal to the given value
            if curr.val <= val:
                # If there is a right child, move to the right child
                if curr.right:
                    curr = curr.right
                # If there is no right child, insert the new node here
                else:
                    curr.right = TreeNode(val)
                    break
            # If the current node's value is greater than the given value
            else:
                # If there is a left child, move to the left child
                if curr.left:
                    curr = curr.left
                # If there is no left child, insert the new node here
                else:
                    curr.left = TreeNode(val)
                    break
        
        # Return the root of the tree
        return root


# Time Complexity: O(log(n))
# Space Complexity: O(1)