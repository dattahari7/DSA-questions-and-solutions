# Bottom View of Binary Tree


# Optimal Solution

from collections import defaultdict
class Solution:
    def bottomView(self, root):
        # Initialize an empty list to store the result
        res = []
        
        # If the root is None, return an empty result list
        if not root:
            return res
        
        # Dictionary to hold the last node encountered at each horizontal distance (x-coordinate)
        view = defaultdict()
        
        # Queue for level-order traversal; stores tuples of (node, x-coordinate)
        que = deque([(root, 0)])
        
        while que:
            # Dequeue the next node along with its x-coordinate
            node, x = que.popleft()
            
            # Update the view dictionary with the current node's data
            view[x] = node.data
            
            # Enqueue the left child with updated x-coordinate if it exists
            if node.left:
                que.append((node.left, x - 1))
                
            # Enqueue the right child with updated x-coordinate if it exists
            if node.right:
                que.append((node.right, x + 1))
        
        # Iterate through the view dictionary sorted by x-coordinates
        for key in sorted(view.keys()):
            # Append the node's data to the result list
            res.append(view[key])
        
        # Return the final result containing the bottom view of the binary tree
        return res


# Time Complexity: O(nlogn)
# Space Complexity: O(n)