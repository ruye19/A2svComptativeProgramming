class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n,m=len(grid),len(grid[0])
        island=0
        def bfs(i,j):
            q=deque()
            q.append((i,j))
            grid[i][j]="0"
            while q:
                x,y = q.popleft()
                for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                    new_x,new_y= x+dx ,y+dy
                    if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == "1":
                        grid[new_x][new_y]="0" 
                        q.append((new_x,new_y))
                    
        for i in range(n):
           for j in range(m):
             if grid[i][j]== "1":
                island+=1
                bfs(i,j)
        return island         
        
        