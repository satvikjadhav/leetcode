"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Ensure k is within the bounds of the list length
        k = k % len(nums)

        # If k is 0, no rotation is needed, so just return the original array
        if k == 0:
            return nums

        # Create a temporary array to store the last k elements
        temp_arr = nums[-k:]

        # Set up a counter starting at the last index of the list
        counter = len(nums) - 1
        
        # Move the elements from the start of the list to the right by k positions
        # This part effectively shifts the first len(nums)-k elements to the right
        for i in range(len(nums)-k-1, -1, -1):
            nums[counter] = nums[i]
            counter -= 1  # Decrease the counter to move backward through the list

        # Replace the first k elements of 'nums' with the elements stored in temp_arr
        nums[:k] = temp_arr

        # Return the modified list (this is optional as the modification is done in-place)
        return nums
