class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = 0
        for i in range(k):
            window += nums[i]
        maxumim = window      
        for j in range(k, len(nums)):
            window = window - nums[j - k] + nums[j] 
            maxumim = max(window , maxumim)
        return  maxumim / k       