class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = defaultdict(lambda:1)
        def dp(index):
            if index not in memo:
                for j in range(index + 1, len(nums)):
                   if nums[j] > nums[index]:
                        memo[index] = max(1 + dp(j), memo[index])
            return memo[index]    

        max_ = 0 
        for i in range(len(nums)):
            max_= max(max_, dp(i))
        return max_     



        