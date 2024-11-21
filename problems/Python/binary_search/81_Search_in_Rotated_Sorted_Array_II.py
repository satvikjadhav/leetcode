"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Get the length of the input array
        n = len(nums)
        
        # Initialize low and high pointers to the start and end of the array
        low = 0
        high = n - 1
       
        # Binary search with handling for duplicates
        while low <= high:
            # Calculate the middle index
            mid = (low + high) // 2
            
            # Special case: when low, mid, and high elements are the same
            if nums[low] == nums[mid] == nums[high]:
                # Check if the middle element is the target
                if nums[mid] == target:
                    return True
                # If not, eliminate duplicates by moving pointers
                else:
                    low += 1
                    high -= 1
                    continue
           
            # Determine which half of the array is sorted
            # Left half is sorted
            if nums[low] <= nums[mid]:
                # Check if target is in the sorted left half
                if nums[mid] == target:
                    return True
                elif nums[low] <= target <= nums[mid]:
                    # Target is in the sorted left half, search left
                    high = mid
                else:
                    # Target is not in the sorted left half, search right
                    low = mid + 1
            
            # Right half is sorted
            elif nums[high] >= nums[mid]:
                # Check if target is in the sorted right half
                if nums[mid] == target:
                    return True
                elif nums[mid] <= target <= nums[high]:
                    # Target is in the sorted right half, search right
                    low = mid
                else:
                    # Target is not in the sorted right half, search left
                    high = mid - 1
        
        # Target not found
        return False