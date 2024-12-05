class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        k=1
        curr=nums[0]
        for i in range(1,len(nums)):
            if curr!=nums[i]:
                nums[k]=nums[i]
                curr=nums[i]
                k+=1
            else:
                nums[i]='_'
        return k

        