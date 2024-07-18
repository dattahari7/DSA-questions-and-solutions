# Merge Sort: Efficient and stable sort, good for large data, requires extra space.

# Merge Sort is a divide-and-conquer algorithm that divides the array into halves, recursively sorts them, and then merges the sorted halves.

def merge_sort(arr):
    if len(arr) > 1:  # Base case: if the array has more than one element
        mid = len(arr) // 2  # Find the middle point to divide the array into two halves
        left_half = arr[:mid]  # Left half
        right_half = arr[mid:]  # Right half

        merge_sort(left_half)  # Recursively sort the left half
        merge_sort(right_half)  # Recursively sort the right half

        # Merge the two halves
        i = j = k = 0

        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print(arr)  # Output: [5, 6, 7, 11, 12, 13]



# Time complexity: O(nlogn) 

# Reason: At each step, we divide the whole array, for that logn and we assume n steps are taken to get a sorted array, so overall time complexity will be nlogn

# Space complexity: O(n)  

# Reason: We are using a temporary array to store elements in sorted order.

# Auxiliary Space Complexity: O(n)