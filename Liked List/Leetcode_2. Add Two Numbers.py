# 2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Initialize a dummy head node to simplify the list manipulation.
        dummy_head = ListNode(-1)
        curr = dummy_head  # Pointer to traverse the result list.
        carry = 0  # Initialize carry to 0.

        # Step 2: Traverse both input lists and add corresponding nodes.
        while l1 or l2:
            # Calculate the sum of current digits along with carry.
            sum = carry
            if l1: sum += l1.val
            if l2: sum += l2.val

            # Calculate the digit and carry for the current position.
            digit = sum % 10
            carry = sum // 10

            # Create a new node with the calculated digit and append it to the result list.
            newNode = ListNode(digit)
            curr.next = newNode
            curr = curr.next  # Move the current pointer to the newly added node.

            # Move to the next nodes in both input lists if they exist.
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        # Step 3: Add the remaining carry if any.
        if carry:
            newNode = ListNode(carry)
            curr.next = newNode

        # Step 4: Return the head of the result list.
        head = dummy_head.next  # Get the head of the result list.
        dummy_head.next = None  # Disconnect the dummy head to avoid memory leak.
        return head

    
# Time Complexity: O(n)
# Space Complexity: O(1)