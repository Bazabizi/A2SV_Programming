class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = defaultdict(int)
        direction = [(1, -1) , (1, 0) , (1 , 1)]
        
        def inbound(row , col):
            return 0 <= row < len(matrix) and 0 <= col < len(matrix)
        
        def lastrow(row):
            return row == len(matrix) - 1

        def dp(row , col):
            if (row , col) in memo:
                return memo[(row , col)]
        
            if lastrow(row):
                return matrix[row][col]
        
            value = float('inf')
            for r , c in direction:
                r += row
                c += col
                if inbound(r , c):
                    value = min(value , dp(r , c))
            
            memo[(row , col)] = matrix[row][col] + value
            return memo[(row , col)]
    
        ans = float('inf')
        
        for col in range(len(matrix)):
            ans = min(ans , dp(0 , col))
        
        return ans