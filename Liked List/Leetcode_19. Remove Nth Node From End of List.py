# 19. Remove Nth Node From End of List

# Bruteforce solution(Naive approch)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Calculate the length of the linked list.
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        # Step 2: Handle the case where the first node needs to be removed.
        if length == n:
            newHead = head.next  # Store the new head after removing the first node.
            head.next = None  # Disconnect the first node from the list.
            return newHead  # Return the new head.

        # Step 3: Calculate the position of the node to be removed from the start.
        res = length - n
        
        # Step 4: Traverse the list to find the node before the one to be removed.
        curr = head
        prev = None
        while curr:
            res -= 1
            if res == 0:  # If the previous node is found (one before the node to remove).
                break
            prev = curr
            curr = curr.next

        # Step 5: Remove the nth node from the end of the list.
        delNode = curr.next  # Node to be deleted.
        curr.next = curr.next.next  # Remove the node by skipping it.
        delNode.next = None  # Disconnect the deleted node from the list.

        # Step 6: Return the head of the modified list.
        return head
    
# Time Complexity: O(n)
# Space Complexity: O(1)

        
        
        

# Optimal solution
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create two pointers, fastp and slowp
        fastp = head
        slowp = head

        # Move the fastp pointer N nodes ahead
        for i in range(n):
            fastp = fastp.next

        # If fastp becomes None, the Nth node from the end is the head
        if fastp is None:
            return head.next

        # Move both pointers until fastp reaches the end
        while fastp.next is not None:
            fastp = fastp.next
            slowp = slowp.next

        # Delete the Nth node from the end
        delNode = slowp.next
        slowp.next = slowp.next.next
        delNode = None
        return head
            
# Time Complexity: O(n)
# Space Complexity: O(1)