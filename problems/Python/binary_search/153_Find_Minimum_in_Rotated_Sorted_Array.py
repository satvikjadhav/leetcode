"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_num = float('inf')
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high: 
            mid = (low + high) // 2 

            # Pick the sorted array, pick the min num, and eliminate it
            # If the left half is sorted
            if nums[low] <= nums[mid]:
                min_num = min(min_num, nums[low])  # Update min_num with left value
                low = mid + 1  # Move the left pointer to the right half
            # If the right half is sorted
            elif nums[high] >= nums[mid]:
                min_num = min(min_num, nums[mid])  # Update min_num with mid value
                high = mid - 1  # Move the right pointer to the left half

        return min_num
