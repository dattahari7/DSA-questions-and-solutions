# 61. Rotate List

# BruteForce solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # If the list is empty, has only one node, or no rotations are needed, return the head
        if not head or not head.next or k == 0:
            return head
        
        # Perform k rotations
        for _ in range(k):
            temp = head
            # Traverse to the second-to-last node
            while temp.next.next:
                temp = temp.next
            # temp.next is now the last node
            new_node = temp.next
            # Remove the last node from the end
            temp.next = None
            # Place the last node at the beginning
            new_node.next = head
            # Update the head to the new node
            head = new_node
        
        # Return the new head after rotations
        return head


# Time Complexity: O(n * k) where n is length of LinkedList.
# Space Complexity: O(1)
    

# Optimal Solution(using length of Liked List)

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # If the list is empty, has only one node, or no rotations are needed, return the head
        if not head or not head.next or k == 0:
            return head
        
        # Calculate the length of the linked list
        len = 1
        tail = head
        while tail.next:
            len += 1
            tail = tail.next
        
        # If k is a multiple of the length, the list remains unchanged
        if k % len == 0:
            return head

        # Connect the tail to the head to make it a circular list
        tail.next = head
        # Calculate the effective rotations needed (k modulo length)
        k = k % len
        # Find the new tail position (len - k steps from the start)
        end = len - k
        while end:
            tail = tail.next
            end -= 1

        # The new head is the node after the new tail
        head = tail.next
        # Break the circular list to form the new list
        tail.next = None

        # Return the new head after rotations
        return head


# Time Complexity: O(n-(n%k)) where n is length of LikedList.
# Space Complexity: O(1)
