class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif left == right:
                return nums[left]    
            else:
                right = mid
                    

        