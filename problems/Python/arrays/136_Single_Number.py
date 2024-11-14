"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ### hashmap solution

        # hashmap = {}

        # for i in range(len(nums)):
        #     if nums[i] in hashmap.keys():
        #         hashmap[nums[i]] += 1
        #     else:
        #         hashmap[nums[i]] = 1

        # for key, value in hashmap.items():
        #     if value == 1:
        #         return key

        ### XOR solution
        unique_number = 0 
        for num in nums:
            unique_number ^= num
            
        return unique_number