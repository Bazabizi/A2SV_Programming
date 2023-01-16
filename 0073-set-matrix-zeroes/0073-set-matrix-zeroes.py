class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        coordinate = set()
        rowSize = len(matrix)
        colSize = len(matrix[0])
        
        for row in range(rowSize):
            for col in range(colSize):
                if matrix[row][col] == 0:
                    coordinate.add((row,col))
        
        
        for row , col in coordinate:
            for j in range(colSize):
                matrix[row][j]= 0
            for i in range(rowSize):
                matrix[i][col] =0
        