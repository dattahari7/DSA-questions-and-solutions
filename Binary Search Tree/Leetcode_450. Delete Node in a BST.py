# 450. Delete Node in a BST

# Optimal Solution

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # If the tree is empty, return None
        if not root:
            return None

        def helper(node):
            # If the node has no left child, return its right child
            if node.left is None:
                return node.right
            # If the node has no right child, return its left child
            elif node.right is None:
                return node.left
            # If the node has both children, find the rightmost node in the left subtree
            rightChild = node.right
            lastRight = findLastRight(node.left)
            # Connect the right subtree to the rightmost node in the left subtree
            lastRight.right = rightChild
            # Return the left child of the node
            return node.left
        
        def findLastRight(node):
            # Find the rightmost node in the subtree
            if node.right is None:
                return node
            return findLastRight(node.right)

        # If the root node is the node to be deleted
        if root.val == key:
            return helper(root)

        temp = root
        while root:
            # Traverse the tree to find the node to be deleted
            if root.val > key:
                # If the left child is the node to be deleted
                if root.left and root.left.val == key:
                    # Replace the left child with the result of helper
                    root.left = helper(root.left)
                    break
                else:
                    root = root.left
            else:
                # If the right child is the node to be deleted
                if root.right and root.right.val == key:
                    # Replace the right child with the result of helper
                    root.right = helper(root.right)
                    break
                else:
                    root = root.right
                    
        # Return the root of the tree
        return temp


# Time Complexity: O(H) here H is Height of BST
# Space Complexity: O(1)