class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
      
        result = ''.join(nums)
        return '0' if result[0] == '0' else result
