class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m=len(grid),len(grid[0])
        island=0


        def dfs(i,j):
            if i<0 or i>=n or j>=m or j<0 or grid[i][j]!="1":
               return
            else:
                grid[i][j] = "0"
                dfs(i,j+1)  
                dfs(i+1,j)  
                dfs(i,j-1)  
                dfs(i-1,j)  
                    

                
        for i in range(n):
           for j in range(m):
             if grid[i][j]== "1":
                island+=1
                dfs(i,j)
        return island         