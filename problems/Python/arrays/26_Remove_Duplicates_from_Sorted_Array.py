"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        unique_index = 0  # Pointer for the position of unique elements
        
        for i in range(1, len(nums)):
            if nums[unique_index] != nums[i]:  # Check for a new unique value
                unique_index += 1  # Move to the next position
                nums[unique_index] = nums[i]  # Update the list in place
        
        return unique_index + 1  # Length of unique elements
    