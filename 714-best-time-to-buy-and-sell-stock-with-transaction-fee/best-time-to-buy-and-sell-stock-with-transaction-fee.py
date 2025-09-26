class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dp(i, h):
            if i == len(prices):
                return 0 
                    
            if not h:
                return max(-prices[i] + dp(i + 1, True),dp(i + 1, h))
            else:
                return max(prices[i] - fee + dp(i + 1, False), dp(i + 1, h)) 

        return dp(0, False)