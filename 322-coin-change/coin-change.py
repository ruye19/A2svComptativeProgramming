class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(i,amount):
            if amount == 0:
                return 0
            if (i == len(coins) and amount > 0) or amount < 0 :
                return float('inf') 
           
            return min(1 + dp(i, amount - coins[i]), dp(i+1, amount))  
        h = dp(0,amount)    
        return h if h != float('inf') else -1 