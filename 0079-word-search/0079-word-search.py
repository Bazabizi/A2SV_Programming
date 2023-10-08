class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        starter = []
        row = len(board)
        col = len(board[0])
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    starter.append((r , c))
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def inbound(row , col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        def backtrack(row , col , idx , path):
            if idx >= len(word):
                return True
            val = False
            for r , c in directions:
                r += row 
                c += col
                if inbound(r , c) and board[r][c] == word[idx] and (r , c) not in path:
                    path.add((r , c))
                    val |= backtrack(r , c , idx + 1 , path)
                    path.remove((r,c))
                    
            return val
        ans = False
        for row , col in starter:
            ans |= backtrack(row , col , 1 , set([(row , col)]))
        
        return ans