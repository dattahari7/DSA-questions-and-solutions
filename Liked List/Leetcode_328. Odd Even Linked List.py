# 328. Odd Even Linked List

# Bruteforce solution
from collections import deque

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list is empty or has only one element, return the head as is.
        if head is None or head.next is None:
            return head

        # Initialize a deque to store node values.
        q = deque()

        # Pointer to traverse the list.
        curr = head

        # Traverse the list to collect values of nodes at odd positions.
        while curr and curr.next:
            q.append(curr.val)  # Add the current node's value to the deque.
            curr = curr.next.next  # Move to the node at the next odd position.
        
        # If the list has an odd number of nodes, add the last node's value.
        if curr:
            q.append(curr.val)

        # Reset the pointer to the second node (first even position).
        curr = head.next
        
        # Traverse the list to collect values of nodes at even positions.
        while curr and curr.next:
            q.append(curr.val)  # Add the current node's value to the deque.
            curr = curr.next.next  # Move to the node at the next even position.
        
        # If the list has an odd number of nodes, add the last node's value.
        if curr:
            q.append(curr.val)

        # Reset the pointer to the head of the list to start rearranging.
        curr = head

        # Reassign values to the nodes from the deque in order.
        while curr:
            curr.val = q.popleft()  # Pop values from the deque and assign to current node.
            curr = curr.next  # Move to the next node.
        
        # Return the modified head of the list.
        return head

# Time Complexity: O(n)
# Space Complexity: O(n)
    


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list is empty or has only one element, return the head as is.
        if head is None or head.next is None:
            return head

        # Initialize pointers for odd and even nodes.
        odd = head  # Pointer to the first odd node (head).
        even = head.next  # Pointer to the first even node.
        evenHead = head.next  # Save the head of the even nodes to link later.

        # Traverse the list to segregate odd and even nodes.
        while even and even.next:
            # Link the current odd node to the next odd node.
            odd.next = even.next
            odd = odd.next  # Move the odd pointer to the next odd node.
            
            # Link the current even node to the next even node.
            even.next = odd.next
            even = even.next  # Move the even pointer to the next even node.

        # After the loop, link the last odd node to the head of the even nodes.
        odd.next = evenHead

        # Return the modified list starting with the head.
        return head

# Time Complexity: O(n)
# Space Complexity: O(1)
