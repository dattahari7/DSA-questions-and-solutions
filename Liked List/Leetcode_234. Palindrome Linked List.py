# 234. Palindrome Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Bruteforce solution (Naive approach)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Initialize a stack to hold the node values
        stack = deque()
        curr = head

        # Traverse the linked list and push all values onto the stack
        while curr:
            stack.append(curr.val)
            curr = curr.next

        # Reset curr to the head of the linked list for a second traversal
        curr = head

        # Traverse the linked list again, this time comparing each value to the top of the stack
        while curr:
            # If the value at the current node does not match the value popped from the stack, it's not a palindrome
            if curr.val != stack.pop():
                return False
            curr = curr.next

        # If all values matched, the linked list is a palindrome
        return True


# Time Complexity: O(n)
# Space Complexity: O(n)


# Optimal solution

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Function to reverse the linked list starting from the given node
        def reverseList(node):
            back = None
            curr = node  # Start from the given node
            while curr:
                front = curr.next
                curr.next = back
                back = curr
                curr = front
            return back

        # Edge case: If the list has only one element, it is a palindrome
        if not head or not head.next:
            return True

        # Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        newHead = reverseList(slow)

        # Compare the first and the reversed second half
        first = head
        second = newHead
        while second:
            if first.val != second.val:
                reverseList(newHead)  # Restore the list before returning
                return False
            first = first.next
            second = second.next

        reverseList(newHead)  # Restore the list after comparison
        return True


# Time Complexity: O(n)
# Space Complexity: O(1)