class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = defaultdict(int)
        visited[(0 ,0)] = grid[0][0]
        queue = deque()
        direction = [(0 ,1 ) , (1, 0) ,(-1, 0) ,(0,-1)]
        def inbound(row , col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        ans = []
        
        queue.append([0 , 0 , grid[0][0]])
        n = len(grid) - 1
        m = len(grid[0]) -1
        
        
        while queue:
            row , col , time = queue.popleft()
            if row == n and col == m:
                heappush(ans , time)
                continue
                # break
            for r , c in direction:
                r += row
                c += col
                if inbound(r , c):
                    if (r , c) not in visited or ((r , c ) in visited and visited[(r ,c)] > time): 
                        newTime = max(time , grid[0][0])
                        queue.append((r , c , max(grid[r][c] , newTime)))
                        visited[(r , c)] = newTime

        return ans[0]