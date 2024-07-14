class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
                    
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            
            current.next = new_node
            new_node.prev = current
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    def insertAt(self, value, position):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        
        if position == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        
        current = self.head
        count = 0
        while current is not None and count < position:
            back = current
            current = current.next
            count += 1
        
        if current is None:
            back.next = new_node
            new_node.prev = back
        else:
            back.next = new_node
            new_node.prev = back
            new_node.next = current
            current.prev = new_node
            
        
    def forword_travers(self):
        print()
        if self.head is None:
            print("Doubly linked list is empty.")
            return
        
        current = self.head
        while current is not None:
            print(current.data, end=" -><- ")
            current = current.next
        print("None")
        
    def backword_travers(self):
        print()
        if self.head is None:
            print("Doubly linked list is empty.")
            return
        current = self.head
        while current.next is not None:
            current = current.next
        
        while current is not None:
            print(current.data, end=" -><- ")
            current = current.prev
        print("None")


dll = DoublyLinkedList()
dll.forword_travers()
dll.backword_travers()
dll.append(3)
dll.append(4)
dll.append(5)
dll.append(6)
print()
print("Traversing after adding node in doubly liked list from end")
dll.forword_travers()
dll.backword_travers()

dll.prepend(2)
dll.prepend(1)
print()
print("Traversing after adding node in doubly liked list from start")
dll.forword_travers()
dll.backword_travers()

print()
print("Inserting node at specified position")
dll.insertAt(2.5, 2)
print("Traversing after adding node in doubly liked list at specific position.")
dll.forword_travers()
dll.backword_travers()

        
    
