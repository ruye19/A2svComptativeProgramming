class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    
        been_here=set()
        for i in range(len(nums)):
            if nums[i] in been_here:
                return True
            been_here.add(nums[i])

            if len(been_here)>k:
                been_here.remove(nums[i-k])
        return False                    
                

        