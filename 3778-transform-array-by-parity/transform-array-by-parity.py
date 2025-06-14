class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        num=[]
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                nums[i]=0
                num.append(nums[i])
            if nums[i]%2 != 0:
                nums[i]=1
                num.append(nums[i])
        num.sort()
        return num            
        