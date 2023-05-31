class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        
        dp = [[0 for _ in range(n)] for i in range(m)]
        dp[0][0]  = 1
        for row in range(m):
            for col in range(n):
                if (row , col) == (0,0) or obstacleGrid[row][col] == 1:
                    continue
                if row - 1 > -1 and obstacleGrid[row - 1][col] == 0:
                    dp[row][col] += dp[row - 1][col]
                if col > 0 and obstacleGrid[row][col - 1] == 0:
                    dp[row][col] += dp[row][col - 1]
        
        return dp[m - 1][n-1]