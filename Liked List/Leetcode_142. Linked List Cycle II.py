# 142. Linked List Cycle II

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while fast != slow and fast:
                    slow = slow.next
                    fast = fast.next
                return slow
            
        return None

# Time Complexity: O(n)
# Space Complexity: O(1)