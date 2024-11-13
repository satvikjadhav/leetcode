"""
Given an array arr[], return the second largest element from an array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the first largest.
"""

class Solution:
    def getSecondLargest(self, arr):
        # Edge case: If the array has fewer than 2 elements, return -1
        if len(arr) < 2:
            return -1
        
        largest = float('-inf')
        second_largest = float('-inf')
        
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num < largest:
                second_largest = num
        
        # If no second largest is found, return -1
        if second_largest == float('-inf'):
            return -1
        return second_largest
