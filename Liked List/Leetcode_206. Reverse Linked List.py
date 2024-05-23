# 206. Reverse Linked List

# Bruteforce solution or Naive solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = [] #create empty stack you can use deque class to create it
        curr = head
        while curr:
            stack.append(curr.val) #adding node value in stack
            curr = curr.next
        curr = head
        while curr:
            curr.val = stack.pop() # assigning back the values to node
            curr = curr.next
        return head
    
# Time Complexity: O(n)
# Space Complexity: O(n)

# optimal solution using iteration

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        back = None
        curr = head
        while curr:
            front = curr.next
            curr.next = back
            back = curr
            curr = front
        return back
    
# Time Complexity: O(n)
# Space Complexity: O(1)
    

# Recursive Solution

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node: Optional[ListNode]) -> Optional[ListNode]:
            # Base case: if the list is empty or has one node, it's already reversed
            if not node or not node.next:
                return node
            
            # Recursively reverse the rest of the list
            newHead = helper(node.next)
            
            # Make the next node point to the current node
            node.next.next = node
            
            # Set the current node's next pointer to None
            node.next = None
            
            return newHead
        
        return helper(head)
    
# Time Complexity: O(n)
# Space Complexity: O(1) except recursive stack space



