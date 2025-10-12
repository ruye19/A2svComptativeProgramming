class Solution:
    def numSquares(self, n: int) -> int:
        @cache
        def dp(i):
            if i == 0:
                return 0
            count = float('inf')
            for k in range(1, int(sqrt(i) + 1)):
                    count = min(count,1 + dp(i - k * k))
            return count        
        return dp(n)          
                  
        