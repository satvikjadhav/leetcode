"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2  # Find middle element
            
            # If target is found at mid, return index
            if nums[mid] == target:
                return mid
                
            # If target is greater, ignore left half
            elif nums[mid] < target:
                left = mid + 1
                
            # If target is smaller, ignore right half
            else:
                right = mid - 1
                
        # Target not found
        return -1

# Example usage
arr = [2, 3, 4, 10, 40, 50, 60, 70]
target = 10