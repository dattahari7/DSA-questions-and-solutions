# 25. Reverse Nodes in k-Group

# Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to reverse a linked list
        def reverseList(node):
            back = None
            temp = node
            while temp:
                front = temp.next
                temp.next = back
                back = temp
                temp = front
            return back
        
        # Helper function to get the k-th node from the current node
        def getKthNode(temp, k):
            k -= 1
            while temp and k > 0:
                k -= 1
                temp = temp.next
            return temp
        
        # Function to reverse every k-group in the linked list
        def kGroupReverse(head, k):
            temp = head
            prevLast = None
            while temp:
                # Get the k-th node from the current node
                kThNode = getKthNode(temp, k)
                # If there are less than k nodes remaining, no more reversing is needed
                if kThNode is None:
                    if prevLast:
                        prevLast.next = temp
                    break
                nextNode = kThNode.next
                # Temporarily end the current k-group
                kThNode.next = None
                # Reverse the current k-group
                reverseList(temp)
                # If this is the first group, update the head to the new head after reversing
                if temp == head:
                    head = kThNode
                else:
                    prevLast.next = kThNode
                # Update prevLast to the end of the reversed group
                prevLast = temp
                temp = nextNode
            return head
        
        # Call the kGroupReverse function to start reversing in k-groups
        return kGroupReverse(head, k)


# Time Complexity: O(n)
# Space Complexity: O(1)