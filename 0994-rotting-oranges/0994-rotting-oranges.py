class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()
        visited = set()
        rowLength = len(grid)
        colLength = len(grid[0])
        def inbound(row , col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        find  = False
        for row in range(rowLength):
            for col in range(colLength):
                if grid[row][col] == 2:
                    queue.append((row,col))
                if grid[row][col] == 1:
                    find = True
        if not find and  not queue:
            return 0
        ans = -1
        while queue:
            size = len(queue)
            for _ in range(size):
                row , col = queue.popleft()
                visited.add((row,col))
                for r , c in directions:
                    r += row
                    c += col
                    if inbound(r , c) and (r,c) not in visited and grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r, c))
            ans += 1
        
        for row in range(rowLength):
            for col in range(colLength):
                if grid[row][col] == 1:
                    return -1
        
        return ans