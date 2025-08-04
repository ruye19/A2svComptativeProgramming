class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[0] * len(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                index=(i+nums[i])%len(nums)
                result[i]= nums[index]
            elif nums[i]<0:
                index=(i-abs(nums[i]))%len(nums)
                result[i]= nums[index]
            else:
                result[i]=nums[i]
        return result             

        