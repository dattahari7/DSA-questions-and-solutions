# Add 1 to a number represented as linked list

# Bruteforce solution(Naive solution)

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self, head):
        # Returns new head of the linked List.
        def reverseList(node):
            back = None
            curr = node
            while curr:
                front = curr.next
                curr.next = back
                back = curr
                curr = front
            return back

        # Reverse the linked list
        newHead = reverseList(head)

        # Add one to the reversed list
        carry = 1
        curr = newHead
        while curr:
            curr.data = curr.data + carry
            if curr.data < 10:
                carry = 0
                break
            else:
                curr.data = 0
                carry = 1

            prev = curr
            curr = curr.next

        # If carry is still 1 after processing all nodes, add a new node
        if carry == 1:
            newNode = Node(1)
            prev.next = newNode

        # Reverse the list back to its original order
        head = reverseList(newHead)
        return head

# Time Complexity: O(3n)
# Space Complexity: O(1)
    

# Recursive solution

class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        def helper(node):
            if not node:
                return 1
            carry = helper(node.next)
            node.data += carry
            if node.data < 10:
                return 0
            node.data = 0
            return 1
        
        carry = helper(head)
        if carry == 1:
            newNode = Node(1)
            newNode.next = head
            head = newNode
        return head


# Time Complexity: O(n)
# Space Complexity: O(n)
