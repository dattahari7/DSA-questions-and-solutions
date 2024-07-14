# Insertion Sort: Builds the sorted array one element at a time by inserting elements into their correct position.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage:
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))  # Output: [5, 6, 11, 12, 13]


# Time Complexity:
#     Best Case: O(n)
#     Average Case: O(n^2)
#     Worst Case: O(n^2)

# Space Complexity:
#     O(1) (In-place sort)