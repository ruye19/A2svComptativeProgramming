class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows=len(grid)
        cols=len(grid[0])
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j >=cols or grid[i][j]!=1:
                return 0
            else:
                grid[i][j]=0
                area=1
                for dr,dc in direction:
                    new_row,new_col=i+dr,j+dc
                    area+=dfs(new_row,new_col)
                return area    
        max_area=0        
        for i in range(rows):
            for j in range(cols):
                    if grid[i][j]== 1:
                        area=dfs(i,j)
                        max_area=max(area,max_area)
        return max_area

