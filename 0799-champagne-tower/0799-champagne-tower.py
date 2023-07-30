class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glass = []
        for row in range(query_row + 1):
            cur_glass = [0]*(row + 1)
            glass.append(cur_glass)
        
        glass[0][0] = poured
        
        for row in range(query_row ):
            for col in range(row+1):
                
                val = (glass[row][col] - 1)/2
                if val < 0:
                    val = 0
                glass[row + 1][col] += val
                glass[row + 1][col + 1] += val
           
        ans = glass[query_row][query_glass]
        
        if glass[query_row][query_glass] > 1:
            ans = 1
        
        return ans
        