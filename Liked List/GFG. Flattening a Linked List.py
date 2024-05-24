# Flattening a Linked List

# BruteForce solution
'''
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None  # Pointer to the next node in the same row
        self.bottom = None  # Pointer to the next node in the same column
'''

def flatten(root):
    # Create an array to store all node values
    arr = []
    temp = root
    
    # Traverse the linked list to collect all values
    while temp:
        t2 = temp
        while t2:
            arr.append(t2.data)  # Add each node's data to the array
            t2 = t2.bottom  # Move to the next node in the column
        temp = temp.next  # Move to the next node in the row
    
    # Sort the collected values
    arr.sort()
    
    # Convert the sorted values back into a flattened linked list
    return convert(arr)
    
def convert(arr):
    # If the array is empty, return None
    if len(arr) == 0:
        return None
    
    # Create the head of the new list with the first value in the array
    head = Node(arr[0])
    temp = head
    
    # Traverse the array and create nodes for each value
    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        temp.bottom = new_node  # Link the new node to the bottom of the current node
        temp = temp.bottom  # Move to the new node
    
    # Return the head of the flattened list
    return head


# Time Complexity: O(m * n) here m is parent list and n is child list
# Space Complexity: O(m * n)


# Optimal solution
'''
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None  # Pointer to the next node in the same row
        self.bottom = None  # Pointer to the next node in the same column
'''

def flatten(root):
    # Base case: if the list is empty or has only one row, return it as is
    if not root or not root.next:
        return root
    
    # Recursively flatten the list starting from the next row
    merged_head = flatten(root.next)
    
    # Merge the current row with the flattened rows
    head = mergeLists(root, merged_head)
    
    # Return the head of the merged (flattened) list
    return head

def mergeLists(list1, list2):
    dummy_node = Node(-1)  # Create a dummy node to serve as the head of the merged list
    temp = dummy_node
    
    # Merge the two lists by comparing the data of the nodes
    while list1 and list2:
        if list1.data < list2.data:
            temp.bottom = list1  # Attach list1's node to the merged list
            temp = list1  # Move temp to the next node in list1
            list1 = list1.bottom  # Move list1 to its next bottom node
        else:
            temp.bottom = list2  # Attach list2's node to the merged list
            temp = list2  # Move temp to the next node in list2
            list2 = list2.bottom  # Move list2 to its next bottom node
        temp.next = None  # Ensure the next pointer is None for all nodes
    
    # If there are remaining nodes in list1, attach them to the merged list
    if list1:
        temp.bottom = list1
    
    # If there are remaining nodes in list2, attach them to the merged list
    if list2:
        temp.bottom = list2
    
    # Ensure the next pointer of the first node in the merged list is None
    if dummy_node.bottom:
        dummy_node.bottom.next = None
    
    # Return the merged list, starting from the node after the dummy node
    return dummy_node.bottom

     

# Time Complexity: O(m * n)
# Space Complexity: O(n) using recursive stack space