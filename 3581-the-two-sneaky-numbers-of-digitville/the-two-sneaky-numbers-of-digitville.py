class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        output = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                output.append(nums[i+ 1])
                i += 1
        return output        