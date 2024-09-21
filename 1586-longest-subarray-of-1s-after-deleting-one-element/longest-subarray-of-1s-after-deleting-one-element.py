class Solution(object):
    def longestSubarray( self, nums):
        left = 0
        zero_count = 0
        max_len = 0

        # Sliding window
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            # If we have more than one zero in the window, shrink the window from the left
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Calculate the maximum length of the subarray
            max_len = max(max_len, right - left)
         
        return max_len
 