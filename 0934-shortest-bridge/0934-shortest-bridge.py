class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(0, 1) , (0, -1) , (1, 0) , (-1 , 0)]
        rowLength  = len(grid)
        colLength  = len(grid[0])
        
        def inbound(row , col):
            return  0 <= row < len(grid) and 0 <= col < len(grid[0])
        row = 0 
        col  = 0
        flag = False
        for r in range(rowLength):
            for c in range(colLength):
                if grid[r][c] == 1:
                    row = r
                    col = c
                    break
                    flag = True
            if flag:
                break
        visited = set([(row,col)])
        queue = deque([(row , col)])
        ans = 0
       
        while queue:
            row  , col = queue.popleft()
            flag = False
            for r , c in directions:
                r += row
                c += col
                if inbound(r , c) and (r , c) not in visited and grid[r][c] == 1:
                    
                    visited.add((r , c))
                    queue.append((r , c))    
        temp = list(visited)
        queue = deque(temp)
        ans = 0
        while queue:
            size = len(queue)
            
            for _ in range(size):
                row , col = queue.popleft()
                for r , c in directions:
                    r += row 
                    c += col
                    if inbound(r , c) and (r , c) not in visited and grid[r][c] == 0:
                        visited.add((r , c))
                        queue.append((r , c))
                    if inbound(r , c) and (r , c) not in visited and grid[r][c] == 1:
                        return ans
            ans += 1   
        
        return ans