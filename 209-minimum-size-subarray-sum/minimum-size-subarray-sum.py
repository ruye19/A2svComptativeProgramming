class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        curr=0
        min_count=float('inf')
        for i in range (len(nums)):
            
            curr+=nums[i]
          
            while curr >= target:
                min_count=min(min_count,i-left+1)
                curr-=nums[left]
                left+=1
   
                
        return min_count if min_count != float('inf')  else 0