def selection_sort(arr):
    # Go through each position in the array
    for i in range(len(arr)):
        # Assume the current position has the minimum value
        min_idx = i
        
        # Look through the rest of the array to find if there's anything smaller
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum value with the first position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Example usage
# numbers = [64, 34, 25, 12, 22, 11, 90]
# sorted_numbers = selection_sort(numbers)
# print(sorted_numbers)  # Output: [11, 12, 22, 25, 34, 64, 90]


def bubble_sort(arr):
    n = len(arr)
    
    # Outer loop for number of passes
    for i in range(n):
        # Flag to optimize if array is already sorted
        swapped = False
        
        # Inner loop for comparisons in each pass
        # We subtract i because after each pass, i elements are already sorted at the end
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if they're in wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return arr

def insertion_sort(arr):
    # Start from the second element
    for i in range(1, len(arr)):
        # Element to be inserted
        key = arr[i]
        
        # Start comparing with previous elements
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place key in its correct position
        arr[j + 1] = key
    
    return arr


# Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Step 2: Recursively sort each half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Step 3: Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Merge elements from left and right arrays in a sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Add remaning elements, if any, from both halves

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr
    
# Test the function
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)