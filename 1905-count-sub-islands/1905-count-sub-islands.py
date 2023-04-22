class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        def inbound(row , col):
            return 0 <= row < len(grid1) and 0 <=  col < len(grid1[0])
        
        
        def dfs(row ,col):
            visited.add((row,col))
            temp = True
            for r , c in direction:
                newRow = row + r
                newCol = col + c
                
                if inbound(newRow,newCol) and grid2[newRow][newCol] and (newRow , newCol) not in visited:
                    if not grid1[newRow][newCol]:
                        self.valid = False
                        continue
                    dfs(newRow , newCol)
                    
        
        ans = 0
        row = len(grid2)
        col = len(grid2[0])
        
        for r in range(row):
            for c in range(col):
                self.valid = True
                if grid2[r][c] and grid1[r][c] and (r , c) not in visited:
                    dfs(r , c )
                    if self.valid:
                        ans += 1
        
        return ans
                        
                    