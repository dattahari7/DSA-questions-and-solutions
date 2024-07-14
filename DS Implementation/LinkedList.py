# class Node:
#     def __init__(self, value) -> None:
#         self.data = value
#         self.next = None

# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None

#     def display(self):
#         if self.head is None:
#             print("Linked list is empty.")
        
#         current = self.head
#         while current is not None:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

#     def length(self):
#         count = 0
#         current = self.head
        
#         while current is not None:
#             count += 1
#             current = current.next
        
#         return count
    
#     def search_in_linkedlist(self, target):
#         current = self.head
#         while current is not None:
#             if current.data == target:
#                 return True
#             current = current.next
#         return False
    

#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             return
        
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node
        
    
#     def prepend(self, value):
#         new_node = Node(value)
#         new_node.next = self.head
#         self.head = new_node
    
#     def insertAt(self, value, position):
#         if position < 0:
#             print("Invalid positon")
#             return
        
#         new_node = Node(value)
#         if position == 0 or self.head is None:
#             new_node.next = self.head
#             self.head = new_node
#             return
        
#         current = self.head
#         for _ in range(1, position):
#             if current.next is None:
#                 print("Position exceeds the length of the list.")
#             current = current.next

#         # Insert the new node at the desired position
#         new_node.next = current.next
#         current.next = new_node


#     def deleteAtStart(self):
#         # Check if the list is empty
#         if self.head is None:
#             print("Linked list is empty. No node to delete.")
#             return
#         self.head = self.head.next


#     def deleteAtEnd(self):
#         # Check if the list is empty
#         if self.head is None:
#             print("Linked list is empty. No node to delete.")
#             return
        
#         # If the list has only one node
#         if self.head.next is None:
#             self.head = None
#             return

#         # Traverse the list to find the second-to-last node
#         current = self.head
#         while current.next.next:
#             current = current.next
#         current.next = None

#     def deleteAtPosition(self, position):
#         if position < 0:
#             print("Invalid Position")
#             return
        
#         if position == 0:
#             self.head = self.head.next
#             return
        
#         current = self.head
#         for _ in range(1, position-1):
#             if current.next is None:
#                 print("Position is beyond the end of the list. Cannot delete.")
#                 return
#             current = current.next
#         current.next = current.next.next


    
# linked_list = LinkedList()
# #append node to linked list
# linked_list.append(2)
# linked_list.append(3)
# linked_list.append(4)
# linked_list.append(5)

# #Displaying singly linked list
# linked_list.display()
# print("Linked list length after inserting node at end postion : ",linked_list.length())
# linked_list.prepend(1)
# linked_list.display()
# print("Linked list length after inserting node at start postion: ",linked_list.length())
# linked_list.insertAt(2.5, 2)
# linked_list.insertAt(3.5, 4)
# linked_list.display()
# print("Linked list length after inserting node at specific position : ",linked_list.length())
# linked_list.deleteAtStart()
# linked_list.display()
# print("Linked list length after deleting the node from start position: ",linked_list.length())
# linked_list.deleteAtEnd()
# linked_list.display()
# print("Linked list length after deleting the node from end position: ",linked_list.length())
# linked_list.deleteAtPosition(6)
# linked_list.display()
# print("Linked list length after deleting the node at given position: ",linked_list.length())

# print("Search for value 3 in linked list : ", linked_list.search_in_linkedlist(3))
# print("Search for value 5 in linked list : ", linked_list.search_in_linkedlist(5))




# Python program to reverse a linked list
# Time Complexity : O(n)
# Space Complexity : O(1)

# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            front = current.next
            current.next = prev
            prev = current
            current = front
        self.head = prev

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end="->")
            temp = temp.next


# Driver code
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print ("Given linked list")
llist.printList()
llist.reverse()
print ("\nReversed linked list")
llist.printList()

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)







