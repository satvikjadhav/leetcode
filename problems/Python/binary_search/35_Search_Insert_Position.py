"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index where it would 
be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize two pointers: left at the beginning and right at the end of the list
        left, right = 0, len(nums) - 1

        # Loop while the search space is valid (left index <= right index)
        while left <= right:
            # Find the middle index of the current search range
            mid = (left + right) // 2

            # Check if the middle element is equal to the target value
            if nums[mid] == target:
                return mid  # Target found, return the index

            # If the target is greater than the middle element, move the left pointer right of mid
            elif nums[mid] < target:
                left = mid + 1  # Narrow the search range to the right half

            # If the target is smaller than the middle element, move the right pointer left of mid
            else:
                right = mid - 1  # Narrow the search range to the left half

        # If we exit the loop, the target is not found. The 'left' index is the correct insertion position
        return left
