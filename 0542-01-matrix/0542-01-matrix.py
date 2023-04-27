class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [ (1,0),(-1,0),(0,1),(0,-1) ]
        queue = deque()
        visited = defaultdict(int)
        rowLength = len(mat)
        colLength = len(mat[0])
        for row in range(rowLength):
            for col in range(colLength):
                if mat[row][col] == 0:
                    queue.append((row , col , 0))
                    visited[(row,col)] = 0
        
        def inbound(row , col):
            return 0 <= row < len(mat) and 0 <= col < len(mat[0])
        
        while queue:
            row , col , path = queue.popleft()
            
            for r , c in directions:
                r += row
                c += col
                if inbound(r , c) and (r , c) not in visited:
                    visited[(r, c)] = path + 1
                    queue.append((r , c , path + 1))
        
        ans = [[0 for _ in range(colLength)] for _ in range(rowLength)]
       
        for row in range(rowLength):
            for col in range(colLength):
                ans[row][col] = visited[(row , col)]
        
        return ans
        