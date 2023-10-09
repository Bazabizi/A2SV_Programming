class Solution:
    def knightDialer(self, n: int) -> int:
        grid = [
            [1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9], 
            [-1, 0, -1]
                ]
        
        directions = [(2, 1), (-2, 1), (-2, -1), (2, -1), (1, 2), (-1, 2), (-1, -2), (1, -2)]

        def inbound(row, col):
            return 0 <= row < 4 and 0 <= col < 3
        
        @cache
        def dp(row , col , digit):
            
            if digit == n:
                return 1
            ans = 0
            for r , c in directions:
                r += row
                c += col
                if inbound(r , c) and grid[r][c] != -1:
                    ans += dp(r , c, digit + 1)
            
            return ans
        ans = 0
        for row  in range(4):
            for col in range(3):
                if grid[row][col] != -1:
                    ans += dp(row , col , 1)
        
        return ans %(10**9 + 7)
            