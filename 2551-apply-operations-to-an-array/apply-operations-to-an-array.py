class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                output.append(nums[i]*2)
                nums[i+1]=0
            else:    
               output.append(nums[i]) 
        output.append(nums[len(nums)-1])       
        def zero_check(nums):
            non_zero=0
            for i in range(len(nums)):
                if nums[i]!=0:
                    nums[i],nums[non_zero]=nums[non_zero],nums[i]
                    non_zero+=1
            return nums   
        return zero_check(output)      
        