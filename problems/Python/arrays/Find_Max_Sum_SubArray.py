arr = [1, 4, 2, 10, 23, 3, 1, 0, 20, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def findMaxSumSubarray_PrefixSum(arr, k):  # k is the fixed length of the subarray we are looking for
    # If the array has fewer elements than the desired subarray length, return [-1] and -1 as an error indicator
    if len(arr) < k:
        return [[-1], -1]
    
    prefix_sum = 0  # Running sum of array elements
    prefix_map = {}  # Maps indices to their cumulative sums
    counter = 0  # Current array index
    max_k_subarr_sum = float('-inf')  # Maximum sum found for k-length subarray
    max_start_index = 0  # Starting index of maximum sum subarray

    # Iterate through the array
    for num in arr:
        prefix_sum += num 
        prefix_map[counter] = prefix_sum 

        # Once we reach the k-th element or beyond, we start checking the sums of subarrays of length k
        if counter >= k - 1:           
            # Check if the sum of the current k-length subarray is greater than the current max
            # The sum of a subarray from index (i-k+1) to i is: prefix_map[i] - prefix_map[i-k]
            if prefix_map.get(counter, 0) - prefix_map.get(counter - k, 0) > max_k_subarr_sum:
                # Update the starting index and the max sum
                max_start_index = counter - k + 1  # This is the start index of the subarray
                max_k_subarr_sum = prefix_map.get(counter, 0) - prefix_map.get(counter - k, 0)  # Update the max sum

        counter += 1
    
    return [[max_start_index], max_k_subarr_sum]


## Sliding Window Implementation

def findMaxSumSubarray(arr, k):
    # Input validation: Check if array length is less than required window size
    if len(arr) < k:
        return [[-1], 0]  # Return invalid index and zero sum for invalid input
    
    # Initialize the sum of first k elements as our first window
    curr_sum = sum(arr[:k])
    max_sum = curr_sum  # Best sum found so far
    max_start_index = 0  # Starting index of the best window found
    
    # Slide the window through the array
    # At each step, add new element and remove first element of previous window
    for i in range(k, len(arr)):
        # Sliding window calculation:
        # Add the new element (arr[i])
        # Subtract the element leaving the window (arr[i-k])
        curr_sum = curr_sum + arr[i] - arr[i-k]
        
        # If we found a better sum, update our tracking variables
        if curr_sum > max_sum:
            max_sum = curr_sum
            # Calculate start index: current index - window size + 1
            max_start_index = i - k + 1
    
    # Return [starting index of best window, sum of elements in that window]
    return [[max_start_index], max_sum]
