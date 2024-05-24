# 160. Intersection of Two Linked Lists

# Bruteforce solution

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Traverse the first list
        temp1 = headA
        while temp1:
            # For each node in the first list, traverse the second list
            temp2 = headB
            while temp2:
                # Check if the nodes from both lists are the same (intersection point)
                if temp1 == temp2:
                    return temp2
                temp2 = temp2.next
            temp1 = temp1.next
        # If no intersection is found, return None
        return None


# Time Complexity: O(m + n)
# Space Complexity: O(1)

# Using Hashing
    
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Initialize temp1 to traverse the first list
        temp1 = headA
        # Initialize temp2 to traverse the second list
        temp2 = headB
        # Create a set to store nodes visited from the first list
        seen = set()
        
        # Traverse the first list and add each node to the set
        while temp1:
            seen.add(temp1)
            temp1 = temp1.next
        
        # Traverse the second list
        while temp2:
            # If a node from the second list is in the set, it's the intersection node
            if temp2 in seen:
                return temp2
            temp2 = temp2.next
        
        # If no intersection is found, return None
        return None

# Time Complexity: O(m + n)
# Space Complexity: O(n)


# Difference in lenth solution

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Helper function to calculate the difference in lengths of two linked lists
        def getDifference(head1, head2):
            len2 = len1 = 0
            # Traverse both lists to find their lengths
            while head1 or head2:
                if head1:
                    len1 += 1
                    head1 = head1.next
                if head2:
                    len2 += 1
                    head2 = head2.next
            # Return the difference in lengths
            return len1 - len2
        
        # Helper function to find the intersection node
        def getIntersection(head1, head2):
            # Calculate the difference in lengths
            diff = getDifference(head1, head2)
            # If head2 is longer, advance head2 by the difference
            if diff < 0:
                while diff != 0:
                    head2 = head2.next
                    diff += 1
            # If head1 is longer, advance head1 by the difference
            else:
                while diff != 0:
                    head1 = head1.next
                    diff -= 1
            # Traverse both lists together until the intersection node is found
            while head1 != None:
                if head1 == head2:
                    return head1
                head2 = head2.next
                head1 = head1.next
            # If no intersection is found, return None
            return head1

        # Call the getIntersection helper function with the two list heads
        return getIntersection(headA, headB)


# Time Complexity: O(m + 2n)
# Space Complexity: O(1)
    
# Optimal Solution

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # If both lists are empty, there is no intersection
        if not headA and not headB:
            return None
        
        # Initialize two pointers to traverse both lists
        temp1 = headA
        temp2 = headB

        # Traverse both lists until the two pointers meet
        while temp1 != temp2:
            # If temp1 reaches the end of listA, switch to the head of listB
            temp1 = headB if temp1 == None else temp1.next
            # If temp2 reaches the end of listB, switch to the head of listA
            temp2 = headA if temp2 == None else temp2.next
        
        # When temp1 and temp2 meet, it's either the intersection node or None if there is no intersection
        return temp1


# Time Complexity: O(m + n)
# Space Complexity: O(1)