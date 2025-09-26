class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        def dp(i, h):
            if i == len(prices):
                return 0 
            if (i,h) not in memo:
                if not h:
                    memo[(i,h)] = max(-prices[i] + dp(i + 1, True),dp(i + 1, h))
                else:
                    memo[(i,h)] = max(prices[i] - fee + dp(i + 1, False), dp(i + 1, h)) 
            return memo[(i,h)]
        return dp(0, False)