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
        zeros=[]
        non_Zeros=[]    
        for i in output:
            if i==0:
                zeros.append(i)
            else:
                non_Zeros.append(i)
        return  non_Zeros+zeros            

        