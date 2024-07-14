class MaxHeap:
    def __init__(self, elements = None) -> None:
        if elements is None:
            self.heap = []
        else:
            self.heap = elements
            self.build_heap()

    def heappush(self, element):
        self.heap.append(element)
        self.heapify_up(len(self.heap) - 1)

    def heappop(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is Empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root
    
    def peek(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is Empty")
        return self.heap[0]
    
    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child

        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child
        
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)
    
    def build_heap(self):
        for i in range(len(self.heap)//2 - 1, -1, -1):
            self.heapify_down(i)

# Example usage:
elements = [3, 9, 2, 1, 4, 5]
max_heap = MaxHeap(elements)
print("Max-Heap:", max_heap.heap)  # Output: Max-Heap: [9, 4, 5, 1, 3, 2]

max_heap.heappush(15)
print("Max-Heap after push:", max_heap.heap)  # Output: Max-Heap after push: [15, 9, 5, 1, 4, 2, 3]

print("Removed largest element:", max_heap.heappop())  # Output: Removed largest element: 15
print("Max-Heap after pop:", max_heap.heap)  # Output: Max-Heap after pop: [9, 4, 5, 1, 3, 2]

