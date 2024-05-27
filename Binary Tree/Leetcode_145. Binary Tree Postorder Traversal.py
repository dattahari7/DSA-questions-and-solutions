# 145. Binary Tree Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Helper function to perform post-order traversal
        def postOrder(root, res):
            if not root:
                return  # Base case: if the node is None, return
            postOrder(root.left, res)  # Recur on the left subtree
            postOrder(root.right, res)  # Recur on the right subtree
            res.append(root.val)  # Visit the root node and add its value to the result list
        
        res = []  # Initialize an empty list to store the traversal result
        postOrder(root, res)  # Call the helper function to start post-order traversal
        return res  # Return the result list containing post-order traversal values


# Time Complexity: O(n)
# Space Complexity: O(n) Including stack space for recursion
    

# Iterative Solution (using 2 stack)

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack1 = deque()  # Stack 1 for iterative traversal
        stack2 = deque()  # Stack 2 to store the post-order traversal result
        res = []  # List to store the final result
        
        if not root:
            return res  # If the tree is empty, return the empty result list
        
        stack1.append(root)  # Start with the root node
        
        # Perform iterative traversal to generate post-order sequence
        while stack1:
            root = stack1.pop()  # Pop the top node from stack1
            stack2.append(root)  # Push it onto stack2
            
            # Push the left and right children onto stack1
            if root.left:
                stack1.append(root.left)
            if root.right:
                stack1.append(root.right)
        
        # Pop nodes from stack2 to generate the post-order traversal result
        while stack2:
            res.append(stack2.pop().val)  # Visit each node and add its value to the result list
        
        return res  # Return the final post-order traversal result

# Time Complexity: O(n)
# Space Complexity: O(n) used two stacks
    


# Iterative Solution (using 1 stack)
    
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = deque()  # Stack for iterative traversal
        res = []  # List to store the post-order traversal result
        curr = root  # Start traversal from the root node

        # Continue traversal until there are nodes to process or the stack is not empty
        while curr or stack:
            if curr:
                stack.append(curr)  # Push the current node onto the stack
                curr = curr.left  # Move to the left child
            else:
                # If the current node is None, it means we have traversed the left subtree
                temp = stack[-1].right  # Get the right child of the top node on the stack
                
                if temp is None:
                    # If the right child is None, it means we can visit the top node
                    temp = stack.pop()  # Pop the top node from the stack
                    res.append(temp.val)  # Visit the node and add its value to the result list
                    
                    # Process nodes with right subtrees already visited
                    while stack and temp == stack[-1].right:
                        temp = stack.pop()  # Pop the next node from the stack
                        res.append(temp.val)  # Visit the node and add its value to the result list
                else:
                    curr = temp  # Move to the right child to explore its subtree
        
        return res  # Return the final post-order traversal result

# Time Complexity: O(n)
# Space Complexity: O(n)
    
