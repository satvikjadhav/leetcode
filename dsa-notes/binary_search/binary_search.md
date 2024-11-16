# Binary Search

Binary Search is like finding a word in a dictionary - you don't check every page, you open to the middle and then decide whether to look in the first or second half. Here's how it works:

Key Concepts:
1. Binary Search ONLY works on sorted arrays
2. It divides the search interval in half each time
3. Time complexity is O(log n), much faster than linear search O(n)

Let's see it in action with a simple example:
```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Find middle element
        
        # If target is found at mid, return index
        if arr[mid] == target:
            return mid
            
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
            
        # If target is smaller, ignore right half
        else:
            right = mid - 1
            
    # Target not found
    return -1

# Example usage
arr = [2, 3, 4, 10, 40, 50, 60, 70]
target = 10
```

Let's trace how this works for finding 10 in our array:

Step 1: Initial state
- Array: [2, 3, 4, 10, 40, 50, 60, 70]
- left = 0, right = 7
- mid = (0 + 7) // 2 = 3
- arr[mid] = 10 ✓ Found!

Here's a more complex example where we need multiple steps:
Finding 60:
1. mid = 3, arr[3] = 10 < 60, so look right
2. left = 4, right = 7, mid = 5, arr[5] = 50 < 60, so look right
3. left = 6, right = 7, mid = 6, arr[6] = 60 ✓ Found!

Key things to remember:
1. Always check if your array is sorted first
2. Be careful with the middle calculation to avoid overflow
3. Think about edge cases: empty array, target not found, single element
