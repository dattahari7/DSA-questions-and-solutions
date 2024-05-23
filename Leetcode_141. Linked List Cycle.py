# 141. Linked List Cycle

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                return True
        
        return False
    
# Time Complexity: O(n)
# Space Complexity: O(1)