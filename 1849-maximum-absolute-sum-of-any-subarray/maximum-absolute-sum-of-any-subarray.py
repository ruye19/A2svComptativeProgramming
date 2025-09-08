class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr, overall = nums[0], nums[0]
        curr2, overall2 =  nums[0], nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i] ,(nums[i] + curr))
            overall = max(curr, overall)

        for i in range(1, len(nums)):
            curr2 = min(nums[i] , nums[i] + curr2)
            overall2 = min(curr2, overall2)

        return max(abs(overall), abs(overall2))

     