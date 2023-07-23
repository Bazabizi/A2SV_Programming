class Solution:
    def knightProbability(self, n: int, k: int, row: int, col: int) -> float:
        old_mem = [[0 for _ in range(n)] for __ in range(n)]
        moves = [( -2, 1 ) , (-2 , -1) , ( 2 , 1 ) , (2 , -1)
        ,( 1 , -2) , ( 1 , 2) , ( -1 , -2) , ( -1 , 2)]
        
        def inbound(row , col  , n):
            return 0 <= row < n and 0 <= col < n
        
        old_mem[row][col] = 1
        while k > 0 :
            new_mem = [[0 for _ in range(n)] for __ in range(n)]

            for row in range(n):
                for col in range(n):
                    count = 0
                    for r , c in moves:
                            r += row
                            c += col
                            
                            if inbound(r , c, n) and old_mem[r][c] != 0:
                                count += old_mem[r][c]
                    new_mem[row][col] = count/8 
                    
            old_mem = new_mem
            k -= 1
            
        
        ans = 0
        for val in old_mem:
            ans += sum(val)
        return ans
        