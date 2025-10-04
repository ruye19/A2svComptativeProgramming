class Solution:
    def minimumTotal(self, tri: List[List[int]]) -> int:
        @cache
        def dp(i,j): 
            if i == len(tri) - 1:
                return tri[i][j]
            down = dp(i + 1,j)
            diagonal = dp(i + 1,j + 1)
            return tri[i][j] +  min(down, diagonal)
        return dp(0,0)    
