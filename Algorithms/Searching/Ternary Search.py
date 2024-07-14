# Ternary Search: Divides array into three parts, O(log3 n) time complexity.

def ternary_search(arr, x, low, high):
    if high >= low:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2

        if x < arr[mid1]:
            return ternary_search(arr, x, low, mid1 - 1)
        elif x > arr[mid2]:
            return ternary_search(arr, x, mid2 + 1, high)
        else:
            return ternary_search(arr, x, mid1 + 1, mid2 - 1)

    return -1

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 5
print(ternary_search(arr, x, 0, len(arr) - 1))  # Output: 4


# Time Complexity:
#     Average Case: O(log3 n)
#     Worst Case: O(log3 n)

# Space Complexity:
    # O(1)