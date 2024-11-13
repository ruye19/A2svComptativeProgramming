class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        read=0
        write=0
        while(read< len(nums)):
            if nums[read]!= 0:
                temp=nums[read]
                nums[read]=nums[write]
                nums[write]=temp
                write+=1
            read+=1    

        
        