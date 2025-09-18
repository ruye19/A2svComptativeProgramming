class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1 
            while left < right:  
                cur_sum = nums[i] + nums[left] + nums[right] 
                if abs(cur_sum - target) < abs(closest_sum - target):
                    closest_sum = cur_sum
                if cur_sum < target:
                    left += 1
                elif target == cur_sum:
                    return cur_sum    
                else:
                    right -= 1
        return closest_sum         


