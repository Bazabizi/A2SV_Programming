class Solution:
    def magicSquare(self,matrix):
        val = matrix[0][0]+matrix[0][1]+ matrix[0][2]
        checker = {1,2,3,4,5,6,7,8,9}
        
        for row in range(3):
            total  = 0
            for col in range(3):
                if matrix[row][col] not in checker:
                    return False
                total += matrix[row][col]
                checker.remove(matrix[row][col])
            if total != val:
                return False
        
        # for row
        
        for col in range(3):
            total  = 0
            for row in range(3):
                total += matrix[row][col]
            if total != val:
                return False
        total = 0
        
        # for diagonal
        
        for idx in range(3):
            total += matrix[idx][idx]
        if total != val:
            return False
        
        return True
    
    
    
    
    
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0])<3:
            return 0;
        rowSize = len(grid)
        colSize = len(grid[0])
        row = 0
        col = 0
        ans = 0
        
        
        while rowSize - row >=3:
            col = 0
            while colSize - col >= 3:
                matrix = []
                for r in range(row,row + 3):
                    temp = []
                    for c in range(col, col + 3):
                        temp.append(grid[r][c])
                    matrix.append(temp)
            
                
                if self.magicSquare(matrix):
                    ans +=1
                col +=1
            row +=1
    
        return ans;
    