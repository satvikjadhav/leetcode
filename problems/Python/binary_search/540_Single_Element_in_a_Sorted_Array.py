"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.
"""

from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        low = 1
        high = n - 1

        if len(nums) == 1:
            return nums[0]
        
        if nums[0] != nums[1]:
            return nums[0]

        if nums[-1] != nums[-2]:
            return nums[-1]

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            # Eliminate left half if the pair of duplicate values are on Even, Odd indices
            if (mid % 2 == 1 and nums[mid] == nums[mid-1]) or (mid % 2 == 0 and nums[mid] == nums[mid+1]):
                low = mid + 1
            # Eliminate right half if the pair of duplicate values are on Odd, Even indices
            else:
                high = mid - 1

        return -1