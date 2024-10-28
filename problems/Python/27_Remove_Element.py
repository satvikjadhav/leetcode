'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return len(nums)
        temp_list = []
        pointer = 0

        for i in range(len(nums)):
            if nums[i] != val:
               temp_list.append(nums[i])
               pointer += 1

        for i in range(len(temp_list)):
            nums[i] = temp_list[i]

        return len(temp_list)
    
    ### Better Solution
        # Initialize a new index for the updated list without the value 'val'
        new_length = 0 

        # Iterate over each number in the input list
        for number in nums:
            # If the current number is not the value to remove, update the list
            if number != val:
                # Assign the number to the new index location
                nums[new_length] = number
                # Increment the new length to move to the next index
                new_length += 1

        # Return the new length of the list after all removals are completed
        return new_length