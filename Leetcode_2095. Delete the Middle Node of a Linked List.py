# 2095. Delete the Middle Node of a Linked List

# Optimal solution
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Check if the list is empty or has only one node.
        if not head or not head.next:
            return None  # There is no middle node to delete.

        # Step 2: Initialize two pointers, slow and fast, to find the middle node.
        slow = head  # Slow pointer moves one step at a time.
        fast = head  # Fast pointer moves two steps at a time.
        prev = None  # Pointer to the node before the middle node.

        # Step 3: Traverse the list to find the middle node using slow and fast pointers.
        while fast and fast.next:
            prev = slow  # Update prev to the current slow pointer.
            slow = slow.next  # Move slow pointer one step forward.
            fast = fast.next.next  # Move fast pointer two steps forward.

        # Step 4: Remove the middle node by updating the next pointer of the previous node.
        prev.next = slow.next  # Skip the middle node by updating the next pointer of the previous node.
        slow.next = None  # Disconnect the middle node from the list.

        # Step 5: Return the head of the modified list after deletion.
        return head

# Time Complexity: O(n)
# Space Complexity: O(1)



