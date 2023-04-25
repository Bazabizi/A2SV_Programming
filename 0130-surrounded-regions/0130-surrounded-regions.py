class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        rowLength = len(board)
        colLength = len(board[0])
        
        def inbound(row , col):
            return 0 <= row < len(board) and 0<= col < len(board[0])
            
        def border(row ,col):
            return row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]) - 1
        
        
        def dfs(row , col):
            board[row][col] = "p"
            for r , c in directions:
                newRow = r + row
                newCol = c + col
                
                if inbound(newRow,newCol) and board[newRow][newCol] == "O":
                    dfs(newRow , newCol)
        
        for row in range(rowLength):
            for col in range(colLength):
                if board[row][col] == "O":
                    if border(row , col) :
                        dfs(row, col)
        
        for row in range(rowLength):
            for col in range(colLength):
                if board[row][col] == "p":
                    board[row][col] = "O"
                else:
                    board[row][col] = "X"
        
        
        
        