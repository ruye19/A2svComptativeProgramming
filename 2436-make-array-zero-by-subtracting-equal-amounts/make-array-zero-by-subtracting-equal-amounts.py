class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums=sorted(nums)
        count=0
        for i in range(len(nums)):
            if nums[i]>0:
                x=nums[i]
                for j in range(len(nums)):
                    if nums[j]<=0:
                        nums[j]=0
                    nums[j]=nums[j]-x
                count+=1
                    
        return count            


