# Root to Leaf Paths

# Optimal Solution

class Solution:
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        # Initialize result list
        res = []
        
        # If root is None, return an empty list
        if not root:
            return res
            
        # Helper function to get paths
        def getPaths(node, path, res):
            if node:
                # Append current node data to path
                path.append(node.data)
                
                # If it's a leaf node, append the path to the result list
                if not node.left and not node.right:
                    res.append(list(path))
                
                else:
                    # Recur for the left and right subtrees
                    getPaths(node.left, path, res)
                    getPaths(node.right, path, res)
                    
                # Backtrack to explore other paths
                path.pop()
        
        # Call the helper function with the root node
        getPaths(root, [], res)
        
        # Return the result list containing all paths
        return res

# Time Complexity: O(n)
# Space Complexity: O(n)