class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rowSize = len(grid)-2
        colSize = len(grid[0])-2
        matrix = [[0 for _ in range(colSize)]for _ in range(rowSize)]

        for row in range(rowSize):
            for col in range(colSize):
                maxVal = grid[row][col]
                
                for i in range(row ,row + 3):
                    for j in range(col , col + 3):
                        if grid[i][j] >maxVal:
                            maxVal = grid[i][j]
                matrix[row][col] = maxVal
        
        return matrix