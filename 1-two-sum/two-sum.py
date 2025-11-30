class Solution(object):
    def twoSum(self, nums, target):
        for left in range(len(nums)):
            right = left + 1
            while right < len(nums):
                if nums[left] + nums[right] == target:
                    return [left ,right]
                right += 1
        


            