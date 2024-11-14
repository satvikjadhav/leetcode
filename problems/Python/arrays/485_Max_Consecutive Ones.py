"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_counter = 0
        
        for num in nums:
            if num == 1:
                counter += 1
            else:
                max_counter = max(max_counter, counter)  # Update max when a 0 is encountered
                counter = 0  # Reset counter on 0

        # After loop ends, compare once more in case the array ends with a streak of 1s
        return max(max_counter, counter)