# 148. Sort List

# Bruteforce solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list is empty or has only one node, it's already sorted
        if not head or not head.next:
            return head
        
        # Initialize an empty list to store the node values
        res = []
        curr = head
        
        # Traverse the linked list and append all values to the list 'res'
        while curr:
            res.append(curr.val)
            curr = curr.next
        
        # Sort the list 'res' containing the node values
        res.sort()
        
        # Reset curr to the head of the linked list
        curr = head
        
        # Traverse the linked list again and update each node's value
        # with the sorted values from the list 'res'
        while curr:
            curr.val = res.pop(0)  # Pop the first element from the sorted list and assign it to the current node's value
            curr = curr.next
        
        # Return the head of the sorted linked list
        return head

    

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
    

# Optimal solution
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Function to perform merge sort on the linked list
        def mergeSort(head):
            # Base case: if the list is empty or has only one node, it's already sorted
            if not head or not head.next:
                return head
            # Find the middle of the list
            middle = findMiddle(head)
            left_head = head
            right_head = middle.next
            # Split the list into two halves
            middle.next = None
            # Recursively sort the left half
            left_head = mergeSort(left_head)
            # Recursively sort the right half
            right_head = mergeSort(right_head)
            # Merge the two sorted halves
            return merge(left_head, right_head)

        # Function to merge two sorted linked lists
        def merge(list1, list2):
            dummy_node = ListNode(-1)  # Dummy node to simplify edge cases
            temp = dummy_node
            # Merge nodes from list1 and list2 in sorted order
            while list1 and list2:
                if list1.val < list2.val:
                    temp.next = list1
                    temp = list1
                    list1 = list1.next
                else:
                    temp.next = list2
                    temp = list2
                    list2 = list2.next
            # Attach the remaining nodes from list1 or list2
            if list1:
                temp.next = list1
            else:
                temp.next = list2

            return dummy_node.next

        # Function to find the middle node of the linked list
        def findMiddle(head):
            slow = head
            fast = head.next
            # Move slow by one step and fast by two steps until fast reaches the end
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        # Call mergeSort on the input list
        return mergeSort(head)

# Time Complexity: O(nlog(n))
# Space Complexity: O(1)