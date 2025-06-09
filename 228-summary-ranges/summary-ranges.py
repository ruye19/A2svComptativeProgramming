from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        if not nums:
            return output
        
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                # Range ends here
                if start == nums[i - 1]:
                    output.append(str(start))
                else:
                    output.append(f"{start}->{nums[i - 1]}")
                start = nums[i]
        
        # Add the final range
        if start == nums[-1]:
            output.append(str(start))
        else:
            output.append(f"{start}->{nums[-1]}")
        
        return output
