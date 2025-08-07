class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=(nums[i]*2)
                nums[i+1]=0
            else:    
               nums[i]=nums[i]
          
        def zero_check(nums):
            non_zero=0
            for i in range(len(nums)):
                if nums[i]!=0:
                    nums[i],nums[non_zero]=nums[non_zero],nums[i]
                    non_zero+=1
            return nums   
        return zero_check(nums)      
        