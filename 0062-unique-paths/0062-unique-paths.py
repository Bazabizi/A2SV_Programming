class Solution:
    def __init__(self):
        self.memo = defaultdict(int)
        
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        
        dp = [[0 for _ in range(n)] for i in range(m)]
        dp[0][0]  = 1
        for row in range(m):
            for col in range(n):
                if (row , col) == (0,0):
                    continue
                if row - 1 > -1:
                    dp[row][col] += dp[row - 1][col]
                if col > 0:
                    dp[row][col] += dp[row][col - 1]
        
        return dp[m - 1][n-1]