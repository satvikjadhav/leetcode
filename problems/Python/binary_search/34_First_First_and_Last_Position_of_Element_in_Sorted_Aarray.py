"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""


from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1, -1]
    
    first = last = -1

    n = len(nums)
    low = 0
    high = n - 1

    ## first Occurance
    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            first = mid
            high = mid - 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    if first == -1:
        return [-1, -1]

    low = 0
    high = n - 1
    
    ## Last Occurance
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            last = mid
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return first, last
    

nums = [1,2,3,8,8,8,10,10,10,10,11,15]
target = 8

print(searchRange(nums, target))