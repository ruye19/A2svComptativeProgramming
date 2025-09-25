class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1 for i in range(len(cost) + 1)]
        def dp(i):
            if i <= 1:
                return 0
            if memo[i] == -1:
                memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
            return memo[i]
        return dp(len(cost))    

        