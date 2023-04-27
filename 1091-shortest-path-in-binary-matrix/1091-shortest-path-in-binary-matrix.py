class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        def inbound(row ,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        rowLength = len(grid) - 1
        directions = [ (1,1) , (1,0) , (1,-1) , (0,1) , (0,-1) , (-1,1) , (-1,0) , (-1,-1) ]
        visited = set()
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        queue = deque([(0,0,1)])
        
        while queue:
            row , col , path = queue.popleft()    
            visited.add((row , col))
            
            if row == rowLength and col == rowLength:
                return path
            
            for r , c in directions:
                r += row
                c += col
                
                if inbound(r , c) and grid[r][c] == 0 and (r , c) not in visited:
                    queue.append((r , c , path + 1))
                    visited.add((r , c))
            
        return -1