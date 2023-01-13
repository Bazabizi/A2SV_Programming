class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rowSize = len(matrix)
        colSize = len(matrix[0])
        row = 0
        col = 0
        
        while row < rowSize:
            temp = row
            while row < rowSize - 1 and col < colSize-1:
                if matrix[row][col] != matrix[row+1][col+1]:
                    return False
                row +=1
                col +=1
            col = 0
            row = temp + 1
        if colSize > 1:    
            col = 1
        else:
            return True
        row = 0
        
        while col < colSize :
            temp = col
            while row < rowSize-1 and col < colSize-1:
                if matrix[row][col] !=  matrix[row+1][col+1]:
                    return False
                col +=1
                row +=1
            col = temp+1 
            row = 0
        
        return True