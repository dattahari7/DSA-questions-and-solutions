class MinHeap:
    def __init__(self, elements) -> None:
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
            raise IndexError('Heap is Empty')
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def peek(self):
        if len(self.heap) == 0:
            raise IndexError('Heap is Empty')
        return self.heap[0]

    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)
        
    def build_heap(self):
        for i in range(len(self.heap)//2 - 1, -1, -1):
            self.heapify_down(i)

elements = [3, 9, 2, 1, 4, 5]
min_heap = MinHeap(elements)
print("Min-Heap:", min_heap.heap)  # Output: Min-Heap: [1, 3, 2, 9, 4, 5]

min_heap.heappush(15)
print("Min-Heap after push:", min_heap.heap)  # Output: Min-Heap after push: [1, 3, 2, 9, 4, 5, 15]

print("Removed Smallest element:", min_heap.heappop())  # Output: Removed Smallest element: 1
print("Min-Heap after pop:", min_heap.heap)  # Output: Min-Heap after pop: [2, 3, 5, 9, 4, 15]



    