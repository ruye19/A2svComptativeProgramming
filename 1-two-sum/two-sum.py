class Solution(object):
    def twoSum(self, nums, target):
        
        for j in range(len(nums) ):
            for  i in range(j + 1, len(nums)):
                if nums[j] + nums[i] == target:
                    return[j,i]


            