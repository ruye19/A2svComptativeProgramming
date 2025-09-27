class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [[-1 for _ in range(len(prices) + 2)] for _ in range(2)]
        def dp(i, h):
            if i >= len(prices):
                return 0 
                   
            if memo[h][i] == -1:
                if not h:
                    memo[h][i] = max(-prices[i] + dp(i + 1, True),dp(i + 1, h))
                else:
                    memo[h][i] = max(prices[i]  + dp(i + 2, False), dp(i + 1, h)) 
            return memo[h][i]
        return dp(0, False)