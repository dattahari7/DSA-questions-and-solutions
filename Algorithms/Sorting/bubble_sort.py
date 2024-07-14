# Bubble Sort: Repeatedly swaps adjacent elements if they are in the wrong order until the list is sorted.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]



# Time Complexity:
#     Best Case: O(n) (when the list is already sorted)
#     Average Case: O(n^2)
#     Worst Case: O(n^2)

# Space Complexity:
#     O(1) (In-place sort)