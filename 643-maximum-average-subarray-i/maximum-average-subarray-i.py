class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxFirst=0
        maxx=float('-inf')
        for i in range(k):
            maxFirst+=nums[i]
        l=0
        maxx=maxFirst
        for i in range(k,len(nums)):
            maxFirst=maxFirst-nums[l]+nums[i]
            maxx= max(maxFirst,maxx)
            l+=1
        return maxx/k 


               

