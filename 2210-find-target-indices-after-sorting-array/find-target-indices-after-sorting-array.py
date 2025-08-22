class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            min_idx = i 
            for j in range(i + 1, len(nums)):
                if nums[min_idx] > nums[j]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        output = []    
        for i in range(len(nums)):    
            if nums[i] == target:
                output.append(i)
        return output        




        