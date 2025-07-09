class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        cols=len(grid[0])
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(i,j):
            if i>=row or i<0 or j >=cols or j<0 or grid[i][j] !="1":
                return
            else:
                grid[i][j]="0"
                dfs(i,j+1)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i-1,j)
        island=0
        for i in range(row):
            for j in range(cols):
                if grid[i][j]=="1":
                    island+=1
                    dfs(i,j)            
        return island            