from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Step 1: Compute prefix sums
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        # Step 2: Initialize the deque to store indices of prefix sums
        deque_index = deque()
        min_length = float('inf')
        
        # Step 3: Iterate through each prefix sum
        for j in range(n + 1):
            # While deque is not empty and the condition is satisfied
            while deque_index and prefix_sum[j] - prefix_sum[deque_index[0]] >= k:
                # Calculate the length of the valid subarray
                min_length = min(min_length, j - deque_index.popleft())
            
            # Maintain the deque: Remove indices of prefix sums that are greater than or equal to current prefix_sum[j]
            while deque_index and prefix_sum[j] <= prefix_sum[deque_index[-1]]:
                deque_index.pop()
            
            # Add the current index to the deque
            deque_index.append(j)
        
        # If no valid subarray found, return -1
        return min_length if min_length != float('inf') else -1
