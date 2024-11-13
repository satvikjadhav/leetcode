"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None: 
        
        # Initialize the pointer to track the position of the last non-zero element.
        pointer = 0
        
        # Iterate through the list starting from the second element (index 1).
        for i in range(1, len(nums)):
            
            # If the element at the 'pointer' position is zero and the current element (nums[i]) is not zero,
            # we swap them. This ensures the non-zero element is moved to the 'pointer' position.
            if nums[pointer] == 0 and nums[i] != 0:
                nums[pointer] = nums[i]  # Move the non-zero element to the 'pointer' position
                nums[i] = 0  # Set the current position to zero (since the non-zero element was moved)
                pointer += 1  # Move the pointer forward to the next position for the next non-zero element

            # If the element at the 'pointer' position is not zero and the current element (nums[i]) is zero,
            # we update the pointer to the current index i. This skips the zero element.
            elif nums[pointer] != 0 and nums[i] == 0:
                pointer = i
        
        return nums
