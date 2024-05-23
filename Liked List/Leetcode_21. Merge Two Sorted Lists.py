# 21. Merge Two Sorted Lists

# Optimal Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to simplify edge cases
        dummy_node = ListNode(0)
        temp = dummy_node

        # Traverse both lists and merge them in sorted order
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        
        # Attach the remaining nodes from list1 or list2
        if list1:
            temp.next = list1
        else:
            temp.next = list2

        # Return the merged list, which starts at dummy_node.next
        return dummy_node.next

# Time Complexity: O(n)
# Space Complexity: O(1)