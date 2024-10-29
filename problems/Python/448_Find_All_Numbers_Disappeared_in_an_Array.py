'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
'''

from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing_ints = []
        set_nums = set(nums)

        for i in range(1, len(nums)+1):
            if i in set_nums:
                continue
            else:
                missing_ints.append(i)
        
        return missing_ints