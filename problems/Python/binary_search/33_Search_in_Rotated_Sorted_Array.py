"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers to the beginning and end of the array
        n = len(nums) - 1
        low = 0
        high = n

        # Perform binary search
        while low <= high:
            # Calculate the middle index
            mid = (low + high) // 2

            # Check which half of the array is sorted
            if nums[low] <= nums[mid]:
                # Left half is sorted
                if nums[mid] == target:
                    # If the middle element is the target, return its index
                    return mid
                elif nums[low] <= target <= nums[mid]:
                    # Target is in the sorted left half, narrow the search to this half
                    high = mid
                else:
                    # Target is not in the sorted left half, search in the right half
                    low = mid + 1
                    
            elif nums[high] >= nums[mid]:
                # Right half is sorted
                if nums[mid] == target:
                    # If the middle element is the target, return its index
                    return mid
                elif nums[mid] <= target <= nums[high]:
                    # Target is in the sorted right half, narrow the search to this half
                    low = mid
                else:
                    # Target is not in the sorted right half, search in the left half
                    high = mid - 1
        
        # If we exit the loop, the target is not in the array
        return -1
