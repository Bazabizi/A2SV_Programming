class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pair=0
        column=defaultdict(int)
        size=len(grid)
        
        for row in range(size):
            ans=[]
            for col in range(size):
                ans.append(grid[col][row])
            ans=tuple(ans)
            column[ans] +=1
        
        for num in grid:
            temp=tuple(num[:size])
            if temp in column:
                pair += column[temp]
        
        return pair