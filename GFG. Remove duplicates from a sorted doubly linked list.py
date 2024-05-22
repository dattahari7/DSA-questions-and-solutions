# Remove duplicates from a sorted doubly linked list
# Question Link: https://bit.ly/3FtJUtZ
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        start = head
        while start and start.next:
            front = start.next
            while front and front.data == start.data:
                front = front.next
            start.next = front
            if front:
                front.prev = start
            start = start.next
        return head
        
# Time Complexity: O(n)
# Space Complexity: O(1)