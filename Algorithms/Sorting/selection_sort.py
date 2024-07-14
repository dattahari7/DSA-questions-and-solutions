# Selection Sort: Repeatedly finds the minimum element and moves it to the sorted portion.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage:
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))  # Output: [11, 12, 22, 25, 64]


# Time Complexity:
    # Best Case: O(n^2)
    # Average Case: O(n^2)
    # Worst Case: O(n^2)

# Space Complexity:
    # O(1) (In-place sort)