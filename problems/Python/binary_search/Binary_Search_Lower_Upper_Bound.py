### Lower Bound

"""
Given a sorted array arr[] (with unique elements) and an integer k, 
find the index (0-based) of the largest element in arr[] that is less than or equal to k. 
This element is called the "floor" of k. If such an element does not exist, return -1.
"""

def findFloor(arr, k):
    #Your code here
    low = 0
    high = len(arr) - 1
    
    ans = float('-inf')
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] > k:
            high = mid - 1
        
        elif arr[mid] <= k:
            ans = mid
            low = mid + 1

    
    if ans == float('-inf'):
        return -1
        
    return ans
                


### Upper Bound

def findFloorCeil(arr, k):
    #Your code here

    if not arr:
        return -1, -1
    
    n = len(arr)
    
    # Edge cases
    if k < arr[0]:
        return -1, arr[0]
    if k > arr[n-1]:
        return arr[n-1], -1
        
    # Binary search
    left, right = 0, n-1
    floor = ceil = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == k:
            return arr[mid], arr[mid]
            
        elif arr[mid] < k:
            floor = arr[mid]
            left = mid + 1
            
        else:  # arr[mid] > k
            ceil = arr[mid]
            right = mid - 1
            
    return floor, ceil


arr = [4638, 6977, 19284, 23396, 29178, 30918]
k = 8200

print(findFloorCeil(arr, k))