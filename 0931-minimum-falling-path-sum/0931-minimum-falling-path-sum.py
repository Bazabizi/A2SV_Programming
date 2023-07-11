class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        size = len(matrix)
        
        for row in range(size - 2 , -1 ,-1 ):
            for col in range(size):
                val = matrix[row + 1][col]
                if col > 0:
                    val = min(val , matrix[row + 1][col - 1])
                if col < size - 1:
                    val = min(val , matrix[row + 1][col + 1])
                matrix[row][col] += val
        
        
        return min(matrix[0])
    