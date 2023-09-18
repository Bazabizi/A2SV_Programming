class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        dp = [[0 for _ in range(length)] for _ in range(length)]
        
        dp[0][0] = 1
        
        for row in range(1 , length):
            dp[row][row] = 1
            for col in range(row - 1 , -1 , -1):
                
                if s[row] == s[col]:
                    dp[row][col] = dp[row - 1][col + 1] + 2
                else:
                    dp[row][col] = max(dp[row-1][col] , dp[row][col + 1])
        
        return dp[-1][0]
                        
        
        
        