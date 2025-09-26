class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [[-1 for _ in range(len(coins))] for _ in range(amount)]
        # SC: O(i * amount) = 12 * 10**4 = 120_000bytes
      
        def dp(i, total):
            if total == amount:
                return 0
            if (i == len(coins) and total < amount) or total > amount :
                return float('inf') 
               
            if memo[total][i] == -1:
                memo[total][i] = min(1 + dp(i, total + coins[i]), dp(i+1, total))  
            return memo[total][i]
        h = dp(0, 0)    
        return h if h != float('inf') else -1 