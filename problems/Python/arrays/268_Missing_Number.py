"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # all_nums = set()
        # for i in range(len(nums)+1):
        #     all_nums.add(i)
        
        # for num in all_nums:
        #     if num not in nums:
        #         return num

        ### more efficient method

        output = len(nums)

        for i in range(len(nums)):
            output += i - nums[i]
        
        return output