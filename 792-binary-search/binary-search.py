from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0 
        high = n - 1
        while low <= high:
            i = (low + high) // 2 
            if nums[i] == target:
                return i
            elif nums[i] < target:
                low = i + 1
            else:
                high = i - 1

        return -1
