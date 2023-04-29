class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0 , 1),(0,-1),( 1, 0),(-1 , 0)]
        
        def border(row , col):
            return row == 0 or row == len(maze) - 1 or col == 0 or col == len(maze[0]) - 1
        
        def inbound(row , col):
            return 0 <= row < len(maze) and 0 <= col < len(maze[0])
        
        visited = set(tuple(entrance))
        entrance.append(0)
        queue = deque([entrance])
        ans = -1
        while queue:
            row , col , path = queue.popleft()
            if border(row , col) and (row!= entrance[0] or col != entrance[1]) :
                return path
            
            for r , c in directions:
                r += row 
                c += col
                if inbound(r , c) and (r , c) not in visited and maze[r][c]==".":
                    queue.append((r, c , path + 1))
                    visited.add((r,c ))
         
        return ans