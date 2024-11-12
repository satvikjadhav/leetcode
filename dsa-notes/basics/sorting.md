# Sorting

## Selection Sort

Selection sort is one of the simpler sorting algorithms. Here's how it works:

1. Imagine we have a row of numbers, and we want to sort them from smallest to largest
2. First, we look through the entire list to find the smallest number
3. Swap that smallest number with whatever is in the first position
4. Then look through the remaining unsorted numbers to find the next smallest
5. Put that one in the second position
6. And keep repeating until everything is sorted

Python Example:

```python
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
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)  # Output: [11, 12, 22, 25, 34, 64, 90]
```

The main characteristics of selection sort are:
- Simple to understand and implement
- Works well for small lists
- Not very efficient for large lists (time complexity of O(n²))
- Uses very few swaps compared to other algorithms

### Time Complexity
The time complexity of **selection sort** is **O(n²)**, where \( n \) is the number of elements in the array. 

Here's why:

1. **Selection sort** works by repeatedly finding the minimum element from the unsorted portion of the array and placing it at the beginning.
2. For each element in the array (assuming it’s \( n \) elements), the algorithm scans the remaining unsorted portion to find the smallest element. 
3. This scanning step takes about \( n \) comparisons for the first element, \( n - 1 \) for the second, \( n - 2 \) for the third, and so on.

This gives a total number of comparisons:

\[
n + (n - 1) + (n - 2) + \dots + 1 = \frac{n(n-1)}{2} \approx \frac{n^2}{2}
\]

Asymptotically, this results in **O(n²)** time complexity, since we drop constant factors in Big-O notation.

## Bubble Sort

Basic Concept:
- Bubble sort repeatedly steps through a list
- Compares adjacent elements
- Swaps them if they're in the wrong order
- The larger elements "bubble up" to the end of the list

Here's a simple visualization with numbers [5, 3, 8, 4, 2]:

```python
First pass:
[5, 3, 8, 4, 2] → [3, 5, 8, 4, 2] → [3, 5, 4, 8, 2] → [3, 5, 4, 2, 8]
Second pass:
[3, 5, 4, 2, 8] → [3, 4, 5, 2, 8] → [3, 4, 2, 5, 8]
Third pass:
[3, 4, 2, 5, 8] → [3, 2, 4, 5, 8]
Fourth pass:
[3, 2, 4, 5, 8] → [2, 3, 4, 5, 8]
```

Here's a simple implementation in Python:

```python
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
```

Key characteristics:
1. Time complexity: O(n²) in worst and average cases
2. Space complexity: O(1) as it sorts in-place
3. Stable sorting algorithm (maintains relative order of equal elements)
4. Adaptive (becomes faster for nearly sorted arrays)

## Insertion Sort

Think of it like sorting playing cards in your hand - you pick up one card at a time and insert it into its correct position among the cards you're already holding.

Here's how it works step by step:
- Start with the second element
- Compare it with previous elements
- Insert it in the correct position
- Move forward one element and repeat

Let's visualize sorting [5, 2, 8, 1, 4]:

```python
Initial array: [5, 2, 8, 1, 4]

Pass 1 (consider 2):
[5 | 2, 8, 1, 4] → [2, 5 | 8, 1, 4]

Pass 2 (consider 8):
[2, 5, | 8, 1, 4] → [2, 5, 8 | 1, 4]

Pass 3 (consider 1):
[2, 5, 8, | 1, 4] → [1, 2, 5, 8 | 4]

Pass 4 (consider 4):
[1, 2, 5, 8 | 4] → [1, 2, 4, 5, 8]
```

Here's the Python implementation:

```python
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
```

Key characteristics:
1. Time complexity:
   - Worst case: O(n²)
   - Best case: O(n) when array is already sorted
   - Average case: O(n²)
2. Space complexity: O(1) as it sorts in-place
3. Stable sorting algorithm
4. Adaptive (performs better on partially sorted arrays)
5. Works well for small data sets
6. Good for nearly-sorted data

## Merge Sort
Merge Sort is a **divide-and-conquer** sorting algorithm. It works by breaking down an array into smaller subarrays until each subarray has only one element (which is inherently sorted). Then, it merges these subarrays back together in a sorted order to form the final sorted array.

### Steps of Merge Sort:
1. **Divide** the array into two halves.
2. **Recursively sort** each half.
3. **Merge** the two halves back together in sorted order.

### Characteristics of Merge Sort:
- **Time Complexity**: \(O(n \log n)\) in the best, worst, and average cases.
- **Space Complexity**: \(O(n)\) as it requires additional space for the temporary arrays during the merging step.
- **Stability**: Yes, merge sort is a stable sort, meaning it preserves the relative order of elements with equal values.

### Python Code Example

Here's a Python implementation of merge sort:

```python
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
    sorted_array = []
    i = j = 0
    
    # Merge elements from left and right arrays in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    # Add remaining elements (if any) from both halves
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array

# Test the function
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
```

Another example implementation of Merge Sort in Python: 

```python
def merge(arr, low, mid, high):
    temp = []  # temporary array
    left = low      # starting index of left half of arr
    right = mid + 1   # starting index of right half of arr

    # storing elements in the temporary array in a sorted manner
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # if elements on the left half are still left
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # if elements on the right half are still left
    while right <= high:
        temp.append(arr[right])
        right += 1

    # transferring all elements from temporary to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)      # left half
    merge_sort(arr, mid + 1, high) # right half
    merge(arr, low, mid, high)     # merging sorted halves

# Example usage
if __name__ == "__main__":
    arr = [9, 4, 7, 6, 3, 1, 5]
    n = len(arr)
    
    print("Before sorting array:", *arr)
    merge_sort(arr, 0, n - 1)
    print("After sorting array:", *arr)
```

### Explanation:
- The `merge_sort` function recursively splits the input list until each sublist has only one element.
- The `merge` function combines two sorted lists into one sorted list by comparing elements from both lists.
  
This implementation highlights how merge sort splits the array, sorts each half, and then merges the sorted halves to get the fully sorted array.


## Summary
Even though selection sort, bubble sort, and insertion sort all have a time complexity of \(O(n^2)\), each has unique characteristics that can make it more suitable in specific situations. Here’s a breakdown of when to use each one:

### 1. **Selection Sort**
   - **Characteristics**: Selection sort works by repeatedly finding the minimum element and moving it to the beginning. It is **not stable** (equal elements might not retain their relative order), and it performs \(O(n^2)\) comparisons regardless of the data’s initial state.
   - **When to Use**:
     - **Small arrays**: It has a simple structure and is easy to implement for small datasets.
     - **Memory-limited environments**: Selection sort only needs a constant amount of extra memory (in-place sort).
     - **Minimizing swaps**: Since selection sort performs at most \(n\) swaps, it can be useful in cases where swapping elements is costly, but comparisons are not.

### 2. **Bubble Sort**
   - **Characteristics**: Bubble sort repeatedly steps through the list, swapping adjacent elements if they are in the wrong order. It is **stable** (maintains the relative order of equal elements).
   - **When to Use**:
     - **Nearly sorted data**: Bubble sort is particularly efficient when the list is already nearly sorted, as it has a best-case time complexity of \(O(n)\) if no swaps are needed.
     - **Teaching tool**: Its simplicity makes it popular for introducing sorting algorithms and understanding basic concepts.
     - **Stability required in a small dataset**: Bubble sort is stable, so it can be preferable if you need to preserve the order of equivalent elements in a very small list.

### 3. **Insertion Sort**
   - **Characteristics**: Insertion sort builds the final sorted array one item at a time. It is **stable** and has a best-case time complexity of \(O(n)\) for nearly sorted data.
   - **When to Use**:
     - **Nearly sorted data**: Insertion sort is efficient for lists that are already mostly sorted, as it has a best-case of \(O(n)\).
     - **Small datasets**: It's often used for small arrays because it’s simple and has low overhead.
     - **Adaptive sorting**: Because it adapts to the initial order of the list, insertion sort can be preferable when you expect the list to have only a few elements out of place.

