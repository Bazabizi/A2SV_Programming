class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count = set()
        #to check the row
        
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    if board[row][col] in count:
                        return False
                    else:
                        count.add(board[row][col])
            count.clear()
        # to check the column
        for col in range(9):
            for row in range(9):
                if board[row][col] != ".":
                    if board[row][col] in count:
                        return False
                    else:
                        count.add(board[row][col])
            count.clear()
        
        row = 0
        col = 0
        #to check 3*3
        while row < 9:
            col =0
            
            while col < 9:

                for i in range(row,row +3):
                    for j in range(col, col+3):
                        if board[i][j] != ".":
                            if board[i][j] in count:
                                return False
                            count.add(board[i][j])
                
                col +=3
                count.clear()
            
            row +=3
        
        return True