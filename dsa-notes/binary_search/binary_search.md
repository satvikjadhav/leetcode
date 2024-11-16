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


## Time Complexity

Binary Search has a time complexity of O(log n), where n is the number of elements in the sorted array

Why it's O(log n):

1. Mathematical Proof:
   - At each step, we divide the problem size by 2
   - Starting with n elements:
     * Step 1: n elements
     * Step 2: n/2 elements
     * Step 3: n/4 elements
     * Step 4: n/8 elements
     * And so on until we reach 1

2. To find how many steps (k) we need:
   * n/(2^k) = 1
   * n = 2^k
   * Taking log₂ of both sides:
   * log₂(n) = k

3. Real-world examples show this logarithmic growth:
   * For n = 8 elements: log₂(8) = 3 steps max
   * For n = 16 elements: log₂(16) = 4 steps max
   * For n = 32 elements: log₂(32) = 5 steps max
   * For n = 1,000,000 elements: log₂(1,000,000) ≈ 20 steps max

This is why Binary Search is so efficient - doubling the input size only adds one extra step to the worst-case scenario. This is the definition of logarithmic growth O(log n).
