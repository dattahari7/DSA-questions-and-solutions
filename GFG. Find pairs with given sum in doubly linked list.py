# Find pairs with given sum in doubly linked list
# Question Link: https://bit.ly/3zWPiBj

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        if not head or not head.next:
            return []
            
        tail = head
        while tail.next:
            tail = tail.next
        res = []
        curr = head
        while curr.data < tail.data:
            add = curr.data + tail.data
            if add == target:
                res.append([curr.data, tail.data])
                curr = curr.next
                tail = tail.prev
            elif add < target:
                curr = curr.next
            else:
                tail = tail.prev
            
        
        return res
                
# Time Complexity: O(n)
# Space Complexity: O(1) After leaving the space to store result list