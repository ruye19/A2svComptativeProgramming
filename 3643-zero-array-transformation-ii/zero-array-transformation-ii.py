class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def validate(m):
            diff = [0 for _ in range(len(nums))]
            for i in range(m + 1):
                l, r, value = queries[i]
                diff[l] += value
                if r != len(nums) - 1:
                    diff[r + 1] -= value
                     
            for i in range(1, len(nums)):
                diff[i] += diff[i - 1]         
            
            zero_count = 0
            for i in range(len(nums)):
                if max(nums[i] - diff[i], 0) == 0:
                    zero_count += 1
            return zero_count == len(nums)         

        left, right = -1, len(queries) - 1
        while left <= right:
            mid = (left + right) // 2
            if validate(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left + 1  if left != len(queries) else -1          
        