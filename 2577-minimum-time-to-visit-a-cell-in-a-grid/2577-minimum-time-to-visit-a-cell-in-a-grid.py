class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1: return -1
        
        directions = [(0 ,1),(0 , -1),(1,0),(-1,0)]
        heap = [(0,(0 , 0))]
        rowLength , colLength = len(grid) , len(grid[0])
        
        def inbound(row , col):
            return 0<= row < len(grid) and 0 <= col < len(grid[0])
        
        visited = set()
        
        
        while heap:
            time , node = heappop(heap)
            row , col = node
            if row == rowLength - 1 and col == colLength - 1:
                return time
            if (row ,col) in visited:
                continue
            visited.add((row , col))
            for r , c in directions:
                r += row
                c += col
                if inbound(r , c) and (r , c) not in visited:
                    wait = 0
                    if (grid[r][c] - time )%2 == 0:
                        wait = 1
                    heappush(heap , (max(time + 1 , grid[r][c] + wait) , (r , c)))
                    

            
            