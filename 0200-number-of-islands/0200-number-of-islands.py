class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        ans = 0
        visited = set()
        def inbound( row , col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(visited , row ,col):
            visited.add((row,col))
            
            for r , c in direction:
                newRow = row + r
                newCol = col + c
                if inbound(newRow,newCol) and grid[row][col]=="1" and (newRow ,newCol) not in visited:
                    dfs(visited , newRow , newCol)
                    
        
        row = len(grid)
        col = len(grid[0])
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r , c) not in visited:
                    dfs(visited , r , c)
                    ans += 1
        
        return ans