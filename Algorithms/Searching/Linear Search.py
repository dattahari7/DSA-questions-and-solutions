# Linear Search: Simple, checks every element, O(n) time complexity.

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Example usage:
arr = [2, 4, 0, 1, 9]
x = 1
print(linear_search(arr, x))  # Output: 3


# Time Complexity:
#     Average Case: O(n)
#     Worst Case: O(n)

# Space Complexity:
    # O(1)

