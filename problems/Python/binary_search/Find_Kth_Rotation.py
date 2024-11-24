class Solution:
    def findKRotation(self, nums):
        # code here
        n = len(nums)
        low = 0
        high = n - 1
        min_num = float('inf')
        min_index = -1
        
        while low <= high: 
            mid = (low + high) // 2 

            # Pick the sorted array, pick the min num, and eliminate it
            # If the left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] < min_num:
                    min_index = low
                    min_num = nums[low] # Update min_num with left value
                low = mid + 1  # Move the left pointer to the right half
            # If the right half is sorted
            elif nums[high] >= nums[mid]:
                if nums[mid] < min_num:
                    min_index = mid
                    min_num = nums[mid] # Update min_num with mid value
                high = mid - 1  # Move the right pointer to the left half

        return min_index