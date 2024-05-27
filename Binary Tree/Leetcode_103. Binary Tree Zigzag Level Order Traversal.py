# 103. Binary Tree Zigzag Level Order Traversal

# Optimal Solution

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []  # List to store the result
        if not root:
            return res  # If the root is None, return an empty result list
        
        que = deque()  # Queue for level-order traversal
        que.append(root)  # Enqueue the root
        
        leftToRight = True  # Flag to indicate the direction of traversal
        while que:
            size = len(que)  # Get the current size of the queue (number of nodes in the current level)
            level = [0] * size  # Initialize a list to store the nodes' values in the current level
            
            # Traverse the nodes in the current level
            for i in range(size):
                node = que.popleft()  # Dequeue a node from the front of the queue
                idx = i if leftToRight else (size - 1 - i)  # Calculate the index to store the node's value based on the direction of traversal
                level[idx] = node.val  # Store the node's value in the appropriate index
                
                # Enqueue the left and right children of the current node, if they exist
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
            leftToRight = not leftToRight  # Toggle the direction of traversal for the next level
            res.append(level)  # Add the list of node values for the current level to the result
        
        return res  # Return the final result containing the zigzag level-order traversal

# Time Complexity: O(n)
# Space Complexity: O(n) including resulting List