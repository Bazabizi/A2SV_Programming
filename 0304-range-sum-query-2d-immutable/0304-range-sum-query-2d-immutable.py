class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefixSum = [[0 for i in range(cols+1)] for i in range(rows+1)]
        
        for row in range(rows):
            for col in range(cols):
                total= self.matrix[row][col] + self.prefixSum[row][col+1] + self.prefixSum[row+1][col]
                
                self.prefixSum[row+1][col+1] = total - self.prefixSum[row][col]
               
        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        total  = self.prefixSum[row2+1][col2+1] - self.prefixSum[row1][col2+1] - self.prefixSum[row2+1][col1]
        totalSum = total + self.prefixSum[row1][col1]
        return totalSum
        
        
        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)