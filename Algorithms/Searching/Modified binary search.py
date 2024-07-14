# Modified Binary Search: Variations for specific cases like rotated arrays.

def search_rotated_array(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        if arr[low] <= arr[mid]:
            if arr[low] <= x < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < x <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

# Example usage:
arr = [4, 5, 6, 7, 0, 1, 2]
x = 0
print(search_rotated_array(arr, x))  # Output: 4



# Time Complexity:
#     Average Case: O(log n)
#     Worst Case: O(log n)

# Space Complexity:
    # O(1)

