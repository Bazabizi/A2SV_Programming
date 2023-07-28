class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rowLength = len(grid)
        colLength = len(grid[0])
        
        for row in range(rowLength - 1, -1 , -1):
            for col in range(colLength - 1 , -1 , -1):
                if row == rowLength - 1 and col == colLength - 1:
                    continue
                val = float('inf')
                if row < rowLength - 1:
                    val = min(val , grid[row + 1][col])
                if col < colLength - 1:
                    val = min(val , grid[row][col + 1])
                
                grid[row][col] += val
        
        return grid[0][0]
                
                