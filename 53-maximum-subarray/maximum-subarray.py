class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, overall = nums[0], nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], nums[i] + curr)
            overall = max(curr, overall)
        return overall            