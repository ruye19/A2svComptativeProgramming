class Solution:
    def canCross(self, stones: List[int]) -> bool:
       
        
        start = stones[0]
        destination = stones[-1]
        stones = set(stones)
        @cache
        def dp(leaf, jump):
            if leaf >= destination:
                return leaf == destination
            if leaf not in stones:
                return False
            
            if jump == 0:
                return dp(leaf + jump + 1, jump + 1)
                
            return dp(leaf + jump - 1, jump - 1) or dp(leaf + jump, jump) or dp(leaf + jump + 1, jump + 1)
        return dp(start, 0)    
         
        """
                              |
        __  __     __     __  __    __        ___          __
        0    1      3     5   6     8         12           17
        
        jump = 0
        
        0 + 1
        
        jump = 1
        
        1 - 1, 1, 1 + 1
        
        jump = 2
        
        2 - 1, 2, 2 + 1
        
        jump = 3
        
        3 - 1, 3, 3 + 1
        
        
        """