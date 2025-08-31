class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        total = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                l = r + 1
            total = max(total, r - l + 1)
        return total         

        