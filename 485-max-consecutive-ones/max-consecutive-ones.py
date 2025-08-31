class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = 0
        result = 0
        for r in range(len(nums)):
            total += nums[r]
            if nums[r] == 0:
                total = 0
                right = 0
            else:    
                result = max(total, result)
        return result  
            

        