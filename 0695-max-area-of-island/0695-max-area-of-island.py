class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        self.temp = 0
        self.ans = 0
        def dfs( row , col):
            
            visited.add((row,col))
            self.temp += 1
            
            for r , c in direction:
                newRow = row + r
                newCol = col + c
                
                if inbound(newRow,newCol) and (newRow,newCol) not in visited and grid[newRow][newCol] == 1:
                    dfs(newRow,newCol)
        size = len(grid)
        colLength = len(grid[0])
        
        for row in range(size):
            for col in range(colLength):
                if grid[row][col] == 1 and (row,col) not in visited:
                    dfs(row,col)
                    self.ans = max(self.ans, self.temp)
                    self.temp = 0
        
        return self.ans