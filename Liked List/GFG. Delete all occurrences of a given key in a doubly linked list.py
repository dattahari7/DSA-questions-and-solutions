# Delete all occurrences of a given key in a doubly linked list
# Question Link: https://bit.ly/3zuBr66

class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        # code here
        # edit the linked list
        if not head:
            return None
        
        curr = head
        
        # Handle the case when the head node itself contains the value x
        while curr and curr.data == x:
            new_head = curr.next
            if new_head:
                new_head.prev = None
            curr.next = None
            curr = new_head
            head = new_head
        
        while curr:
            if curr.data == x:
                front = curr.next
                back = curr.prev
                if back:
                    back.next = front
                if front:
                    front.prev = back
                temp = curr
                curr = curr.next
                temp.next = None
                temp.prev = None
            else:
                curr = curr.next
        
        return head
    
# Time Complexity: O(2+n) ~ O(n)
# Space Complexity: O(1)
 