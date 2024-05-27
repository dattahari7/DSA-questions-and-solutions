# 102. Binary Tree Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []  # Initialize an empty list to store the level order traversal result
        if not root:
            return res  # If the tree is empty, return the empty result list
        
        que = deque()  # Initialize a deque for BFS
        que.append(root)  # Start BFS with the root node
        
        while que:
            size = len(que)  # Get the number of nodes at the current level
            level = []  # Initialize a list to store the values of the current level
            
            for i in range(size):  # Iterate through all nodes at the current level
                node = que.popleft()  # Pop the leftmost node
                level.append(node.val)  # Add its value to the level list
                
                if node.left:  # If the left child exists, add it to the queue
                    que.append(node.left)
                if node.right:  # If the right child exists, add it to the queue
                    que.append(node.right)
            
            res.append(level)  # Add the current level list to the result list
        
        return res  # Return the final list containing level order traversal


# Time Complexity: O(n)
# Space Complexity: O(1) excluding result list space

