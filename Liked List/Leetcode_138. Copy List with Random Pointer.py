# 138. Copy List with Random Pointer

# BruteForce Solution (using map/dictonary)

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # If the input list is empty, return None
        if not head:
            return head
        
        # Create a mapping from original nodes to their copies
        mpp = {}
        temp = head
        
        # First pass: create a copy of each node and store it in the mapping
        while temp:
            new_node = Node(temp.val)  # Create a new node with the same value as the original
            mpp[temp] = new_node  # Map the original node to the new node
            temp = temp.next
        
        # Second pass: set the next and random pointers for each copied node
        temp = head
        while temp:
            new_node = mpp[temp]  # Get the copied node from the mapping
            new_node.next = mpp.get(temp.next)  # Set the next pointer
            new_node.random = mpp.get(temp.random)  # Set the random pointer
            temp = temp.next
        
        # Return the head of the copied list
        return mpp[head]

# Time Complexity: O(n)
# Space Complexity: O(n) except space for new resultant list
    

# Optimal Solution

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # First pass: Create new nodes and insert them right after each original node
        temp = head
        while temp:
            new_node = Node(temp.val)  # Create a new node with the same value as the original
            new_node.next = temp.next  # Set the new node's next to the original node's next
            temp.next = new_node  # Insert the new node after the original node
            temp = temp.next.next  # Move to the next original node
        
        # Second pass: Set the random pointers for the new nodes
        temp = head
        while temp:
            new_node = temp.next  # Get the new node
            if temp.random:
                new_node.random = temp.random.next  # Set the new node's random to the copied node
            else:
                new_node.random = None  # If the original random is None, set the new node's random to None
            temp = temp.next.next  # Move to the next original node
        
        # Third pass: Separate the new nodes to form the copied list
        temp = head
        dummy_node = Node(-1)  # Dummy node to help with list construction
        res = dummy_node
        while temp:
            res.next = temp.next  # Set the next of the result list to the new node
            temp.next = temp.next.next  # Restore the original list's next pointer
            res = res.next  # Move to the next node in the result list
            temp = temp.next  # Move to the next original node
        
        # Return the head of the copied list
        return dummy_node.next


# Time Complexity: O(n)
# Space Complexity: O(1) except space for new resultant list
