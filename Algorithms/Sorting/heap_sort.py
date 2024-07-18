# Heap Sort: Efficient, in-place sort, not stable but doesn't require extra space beyond the input array.

# Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure. It's similar to selection sort where we first find the maximum element and place it at the end. We repeat the process for the remaining elements.

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # If left child is larger than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[largest] < arr[right]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected sub-tree

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)  # Heapify root element

# Example usage
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print(arr)  # Output: [5, 6, 7, 11, 12, 13]


# Time Complexity: O(nlogn)
# Space Complexity: 𝑂(1)
