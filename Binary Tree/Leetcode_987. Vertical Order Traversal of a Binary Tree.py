# 987. Vertical Order Traversal of a Binary Tree

# Optimal Solution

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = defaultdict(lambda: defaultdict(list))  # Dictionary to hold nodes grouped by their x and y coordinates

        que = deque([(root, 0, 0)])  # Queue to perform BFS; stores tuples of (node, x-coordinate, y-coordinate)
        while que:
            temp, x, y = que.popleft()  # Dequeue the next node along with its coordinates
            nodes[x][y].append(temp.val)  # Append the node's value to the list at coordinates (x, y)

            # Enqueue the left child with updated coordinates if it exists
            if temp.left:
                que.append((temp.left, x - 1, y + 1))
            # Enqueue the right child with updated coordinates if it exists
            if temp.right:
                que.append((temp.right, x + 1, y + 1))

        res = []  # List to store the result
        # Iterate through the nodes dictionary sorted by x-coordinates
        for x in sorted(nodes.keys()):
            col = []  # List to store the current column's nodes
            # Iterate through the y-coordinates for the current x-coordinate, sorted in ascending order
            for y in sorted(nodes[x].keys()):
                col.extend(sorted(nodes[x][y]))  # Append the sorted list of nodes at (x, y) to the column list
            res.append(col)  # Append the current column to the result list
        return res  # Return the final result containing the vertical order traversal


# Time Complexity: O(n * log(n))
# Space Complexity: O(n) 