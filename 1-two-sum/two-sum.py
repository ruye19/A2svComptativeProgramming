class Solution(object):
    def twoSum(self, nums, target):
        num = {}
        for i in range(len(nums)):
            if target - nums[i] in num:
                return [num[target - nums[i]], i]
            num[nums[i]] = i    
        



            
        


            