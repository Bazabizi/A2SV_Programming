class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        
        row_1=[]
        col_1=[]
        
        for row in range(n):
            num=0
            for col in range(m):
                if grid[row][col]==1:
                    num+=1
            row_1.append(num)
        
        for col in range(m):
            num=0
            for row in range(n):
                if grid[row][col]==1:
                    num+=1
            col_1.append(num)
        
        ans=[]
        print (row_1)
        print(col_1)
        
        for row in range(n):
            temp=[]
            
            for col in range(m):
                num = 2 *(row_1[row] +col_1[col]) - m - n
                temp.append(num)
            ans.append(temp)
            
        return ans
        
        
        