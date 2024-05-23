# 876. Middle of the Linked List

# Bruteforce solution
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        
        midNode = count // 2 + 1
        curr = head
        while curr:
            midNode -= 1
            if midNode == 0:
                break
            curr = curr.next
        
        return curr

# Time Complexity: O(n)
# Space Complexity: O(1)
    
    
# Optimal solution
    
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head  # used [TortoiseHare Method] for this solution
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
# Time Complexity: O(n/2)
# Space Complexity: O(1)
