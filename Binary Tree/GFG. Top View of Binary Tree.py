# Top View of Binary Tree

# Optimal Solution

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

from collections import defaultdict
class Solution:
    
    # Function to return a list of nodes visible from the top view 
    # from left to right in Binary Tree.
    def topView(self, root):
        
        res = []  # List to store the result
        if not root:
            return res  # If the root is None, return an empty result list
        
        que = deque([(root, 0)])  # Queue for level-order traversal; stores tuples of (node, x-coordinate)
        view = defaultdict()  # Dictionary to hold the first node encountered at each horizontal distance (x-coordinate)
        
        while que:
            node, x = que.popleft()  # Dequeue the next node along with its x-coordinate
            if x not in view:  # If the x-coordinate is not yet in the view dictionary, add the node's data
                view[x] = node.data
            # Enqueue the left child with updated x-coordinate if it exists
            if node.left:
                que.append((node.left, x - 1))
            # Enqueue the right child with updated x-coordinate if it exists
            if node.right:
                que.append((node.right, x + 1))
        
        # Iterate through the view dictionary sorted by x-coordinates
        for key in sorted(view.keys()):
            res.append(view[key])  # Append the node's data to the result list
        
        return res  # Return the final result containing the top view of the binary tree


# Time Complexity: O(nlogn)
# Space Complexity: O(n)