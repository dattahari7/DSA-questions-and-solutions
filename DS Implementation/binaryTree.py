from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertNode(root, val):
    if root is None:
        return TreeNode(val)
    
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        
        if node.left is None:
            node.left = TreeNode(val)
            return root
        else:
            queue.append(node.left)
        
        if node.right is None:
            node.right = TreeNode(val)
            return root
        else:
            queue.append(node.right)
    
    return root

# Example usage:
# def printInOrder(root):
#     if root:
#         printInOrder(root.left)
#         print(root.val, end=" ")
#         printInOrder(root.right)


def printPreOrder(node):
    if node is None:
        return
    print(node.val, end=" ")
    printPreOrder(node.left)
    printPreOrder(node.right)

def printInOrder(node):
    if node is None:
        return
    printInOrder(node.left)
    print(node.val, end=" ")
    printInOrder(node.right)

def printPostOrder(root):
    if root is None:
        return
    printPostOrder(root.left)
    printPostOrder(root.right)
    print(root.val, end=" ")

def printLevelOrder(root):
    if root is None:
        return
    
    q = deque()
    q.append(root)

    while q:
        print(q[0].val, end=" ")
        node = q.popleft()

        if node.left is not None:
            q.append(node.left)
        
        if node.right is not None:
            q.append(node.right)


# Create a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Original Binary Tree (In-order traversal):")
printInOrder(root)  # Output: 4 2 5 1 3

# Insert a node into the binary tree
inserted_root = insertNode(root, 6)
print("\nBinary Tree after inserting node with value 6 (In-order traversal):")
printInOrder(inserted_root)  # Output: 4 2 5 1 3 6

print("\nBinary Tree after inserting node with value 6 (pre-order traversal):")
printPreOrder(inserted_root)  #Output: 1 2 4 5 3 6

print("\nBinary Tree after inserting node with value 6 (post-order traversal):")
printPostOrder(inserted_root)  #Output: 1 2 4 5 3 6

print("\nBinary Tree after inserting node with value 6 (level-order traversal):")
printLevelOrder(inserted_root)  #Output: 1 2 3 4 5 6
