class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.ans = 0
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set()
        
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        
        def dfs(grid ,vistied ,row,col):
            if not inbound(row,col) or grid[row][col] == 0:
                
                self.ans += 1
                return 
            
            visited.add((row,col))
            
            for row_change , col_change in direction:
                newRow = row + row_change
                newCol = col +  col_change
                if (newRow,newCol) not in visited:
                    dfs( grid , visited ,newRow, newCol )
            
        check =True
        for row in range(len(grid)):
        
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(grid,visited,row,col)
                    check = False
                    break
            if not check:
                break
        return self.ans