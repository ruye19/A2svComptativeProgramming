class Solution:
    def numDistinct(self, s: str, t: str) -> int:
    
        m, n = len(s), len(t)
        
        # dp[i][j] will store the number of distinct subsequences of s[0:i] that equal t[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # If t is an empty string, there's exactly one way to match it (delete all characters of s)
        for i in range(m + 1):
            dp[i][0] = 1
        
        # Fill the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        # The result is the number of distinct subsequences of s that equal t
        return dp[m][n]


            