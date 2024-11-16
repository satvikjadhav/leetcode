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
    low = 0
    high = len(arr) - 1
    
    floor = float('-inf')
    ceil = float('-inf')
    
    ## floor
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] > k:
            high = mid - 1
        
        elif arr[mid] <= k:
            floor = mid
            low = mid + 1
    
    ## Ceil
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] >= k:
            ceil = mid
            high = mid - 1
        
        elif arr[mid] < k:
            low = mid + 1
    
    if floor == float('-inf'):
        return -1, arr[ceil]
    if ceil == float('-inf'):
        return arr[floor], -1
        
    return arr[floor], arr[ceil]


arr = [4638, 6977, 19284, 23396, 29178, 30918]
k = 8200

print(findFloorCeil(arr, k))