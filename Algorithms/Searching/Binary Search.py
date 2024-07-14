# Binary Search: Efficient for sorted lists, O(log n) time complexity.

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage:
arr = [1, 2, 3, 4, 5]
x = 3
print(binary_search(arr, x))  # Output: 2


# Time Complexity:
#     Average Case: O(log n)
#     Worst Case: O(log n)

# Space Complexity:
    # O(1)

