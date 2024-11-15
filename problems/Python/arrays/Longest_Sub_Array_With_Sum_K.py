"""
Given an array arr[] containing integers and an integer k, 
your task is to find the length of the longest subarray 
where the sum of its elements is equal to the given value k. 
It is guaranteed that a valid subarray exists.
"""

### Brute Solution
def lenOfLongestSubarr_Brute(arr, k):
    # code here for positivies only
    subarrays = []
    i = 0
    max_len = 0
    total = 0
    ## Generate all sub arrays
    ## Time Complexity: O(N^3)
    for i in range(len(arr)):
        for j in range(i, len(arr)+1):
            if not arr[i:j]:
                continue

            subarrays.append(arr[i:j])
    
    
    for subarray in subarrays:
        if sum(subarray) == k:
            max_len = max(max_len, len(subarray))

    ## Time Complexity: O(N^2)
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if not arr[i:j]:
                continue

            total += arr[j]

            if total == k:
                max_len = max(max_len, len(arr[i:j]))


    return max_len

### Better Solution
def lenOfLongestSubarr_Better(arr, k):
    """
    Finds length of longest subarray that sums to k using prefix sum and hashmap.
    
    Strategy:
    1. Keep track of running sum and store in hashMap: {running_sum: index}
    2. At each step, check two things:
       a) If current running sum equals k (subarray from start)
       b) If (running_sum - k) exists in hashMap (subarray in middle)
    3. When we find a valid subarray, compare its length with current max_length
    
    Example: arr = [10,5,2,7,1,9], k = 15
    When we reach index 4 (value 1):
    - running_sum = 25
    - rem = 25 - 15 = 10
    - We saw 10 at index 0
    - Therefore elements from index 1 to 4 [5,2,7,1] sum to 15
    - Length = 4 - 0 = 4
    """

    hashMap = {}
    sum = 0
    max_len = 0
    ## Time Complexity: best/avg= O(N), worst=O(N^2)
    for i in range(len(arr)):
        sum += arr[i]
        if sum == k:
            max_len = max(max_len, i+1)

        # If the running sum minus k exists in our hashMap, it means we've found a valid subarray
        # Example: if current sum = 25 and k = 15, we check if we've seen sum = 10 before
        rem = sum - k

        # If we've seen this remaining sum before, we've found a valid subarray that sums to k
        if rem in hashMap:
            # Length calculation:
            # current_index - index_where_we_saw_rem = length of subarray that sums to k
            # Example: if current_index = 4 (at value 1) and rem_index = 0 (at value 10)
            # Then elements from index 1 to 4 [5,2,7,1] sum to k
            len_of_rem = i - hashMap[rem]
            
            # Update max_len if this subarray is longer
            max_len = max(max_len, len_of_rem)

        # Store current running sum and its index for future calculations
        if sum not in hashMap:
            hashMap[sum] = i
    
    return max_len

### Optimal Solution -- only if positives and 0s
def lenOfLongestSubarr(arr, k):
    ## Two Pointer and greedy approach
    left = 0
    arr_sum = 0
    arr_len = 0

    for i in range(len(arr)):
        arr_sum += arr[i]

        while arr_sum > k and left <= i:
            arr_sum -= arr[left]
            left += 1
        

        if arr_sum == k:
            arr_len = max(arr_len, i+1-left)
    
    return arr_len


arr = [10, 5, 2, 7, 1, 9]
print(lenOfLongestSubarr(arr, 15))