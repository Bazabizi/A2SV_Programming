class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        rows = 3
        cols = len(grid[0]) + 2
        prefixSum = [[0 for _ in range(cols)] for __ in range(rows)]
        
        for c in range(cols - 2, 0 ,-1):
            prefixSum[1][c] = prefixSum[1][c+1] + grid[0][c-1]
        
        for c in range(1,cols-1):
            prefixSum[2][c] = prefixSum[2][c-1] + grid[1][c-1]
        ans = float('inf')
        col = 1 
        while col < cols - 1:
            val = max(prefixSum[1][col + 1] , prefixSum[2][col - 1] )
            ans = min(val,ans)
            col += 1
        return ans