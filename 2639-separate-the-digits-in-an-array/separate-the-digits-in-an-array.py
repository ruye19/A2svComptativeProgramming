class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[]
        for i in range(len(nums)):
            for num in str(nums[i]):
                output.append(int(num))
        return output        
        