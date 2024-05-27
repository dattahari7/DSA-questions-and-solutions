# 545. Boundary of Binary Tree

# Optimal Solution                      
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def isLeaf(self, root):
        """
        Function to check if a node is a leaf
        """
        return not root.left and not root.right

    def addLeftBoundary(self, root, res):
        """
        Function to add the left boundary of the tree
        """
        curr = root.left
        while curr:
            if not self.isLeaf(curr):
                # If the current node is not a leaf,
                # add its value to the result
                res.append(curr.data)
            # Move to the left child if it exists,
            # otherwise move to the right child
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

    def addRightBoundary(self, root, res):
        """
        Function to add the right boundary of the tree
        """
        curr = root.right
        temp = []
        while curr:
            if not self.isLeaf(curr):
                # If the current node is not a leaf,
                # add its value to a temporary vector
                temp.append(curr.data)
            # Move to the right child if it exists,
            # otherwise move to the left child
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        # Reverse and add the values from
        # the temporary vector to the result
        for i in range(len(temp) - 1, -1, -1):
            res.append(temp[i])

    def addLeaves(self, root, res):
        """
        Function to add the leaves of the tree
        """
        if self.isLeaf(root):
            # If the current node is a leaf,
            # add its value to the result
            res.append(root.data)
            return
        # Recursively add leaves of
        # the left and right subtrees
        if root.left:
            self.addLeaves(root.left, res)
        if root.right:
            self.addLeaves(root.right, res)

    def printBoundary(self, root):
        """
        Main function to perform the
        boundary traversal of the binary tree
        """
        res = []
        if not root:
            return res
        # If the root is not a leaf,
        # add its value to the result
        if not self.isLeaf(root):
            res.append(root.data)

        # Add the left boundary, leaves,
        # and right boundary in order
        self.addLeftBoundary(root, res)
        self.addLeaves(root, res)
        self.addRightBoundary(root, res)

        return res

# Helper function to
# print the result
def printResult(result):
    for val in result:
        print(val, end=" ")
    print()

# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

solution = Solution()

# Get the boundary traversal
result = solution.printBoundary(root)

# Print the result
print("Boundary Traversal:", end=" ")
printResult(result)


# Time Complexity: O(n)
# Space Complexity: O(n)