class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if  i == j == 0:
                    continue
                left = up = float('inf')  
                if i != 0:
                    up = grid[i][j] + grid[i - 1][j]
                if j != 0:
                    left = grid[i][j] + grid[i][j - 1]
                grid[i][j] = min(left, up)    
        return grid[m - 1][n- 1]            