class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(goal_sum):
            if goal_sum < 0:
                return 0
            left = 0
            total = 0
            count = 0
            for right in range(len(nums)):
                total += nums[right]
                while total > goal_sum:
                    total -= nums[left]
                    left += 1
                count += (right - left + 1)
                print(total)
            return count     
        return helper(goal) - helper(goal - 1) 