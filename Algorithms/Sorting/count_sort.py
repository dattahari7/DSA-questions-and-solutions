# Count Sort: Very efficient for small range integers, not suitable for large range data.

# Count Sort is an integer sorting algorithm that counts the occurrences of each unique element in the array. It works well when the range of input data is not significantly greater than the number of elements.

def count_sort(arr):
    max_val = max(arr)  # Find the maximum value in the array
    count = [0] * (max_val + 1)  # Initialize the count array
    output = [0] * len(arr)  # Output array to store the sorted elements

    # Store the count of each element
    for num in arr:
        count[num] += 1

    # Change count[i] so that count[i] contains the actual
    # position of this element in the output array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output array
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    # Copy the output array to arr, so that arr now
    # contains sorted elements
    for i in range(len(arr)):
        arr[i] = output[i]

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
count_sort(arr)
print(arr)  # Output: [1, 2, 2, 3, 3, 4, 8]


# Time Complexity: O(n+k), where n is the number of elements and k is the range of the input.

# Space Complexity: O(k)