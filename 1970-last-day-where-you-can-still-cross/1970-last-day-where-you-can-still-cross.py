class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        parent = [i for i in range(row*col + 2)]
        direction = [(0,1) , (1 , 0) , (-1 , 0 ) , (0, -1)]
        length = len(cells)
        size = [1]*(row*col + 2)
        grid = [[1]*col for _ in range(row)]
        
        def inbound(row , col):
            return 0<= row < len(grid) and 0 <= col < len(grid[0])
        
        def find(child):    
            while child != parent[child]:
                parent[child] = parent[parent[child]]
                child = parent[child]
            
            return child
        
        def union(x , y):
            rep_x = find(x)
            rep_y = find(y)
            
            if rep_x != rep_y:
                if size[rep_x] >= size[rep_y]:
                    parent[rep_y] = rep_x
                    size[rep_x] += size[rep_y]
                else:
                    parent[rep_x] = rep_y
                    size[rep_y] += size[rep_x]
        
        
        for idx in range(length - 1, -1 , -1):
            r , c = cells[idx][0] - 1 , cells[idx][1] - 1
            position1 = r*col + c + 1
            grid[r][c] = 0
            for new_row , new_col in direction:
                new_row += r
                new_col += c
                position2 = new_row*col + new_col + 1
                if inbound(new_row , new_col) and grid[new_row][new_col] == 0:
                    union(position1 , position2)
            
            if r == 0:
                union( 0 , position1)
            elif r == row - 1:
                union( row*col + 1 , position1)
            
            if find(0) == find(row * col + 1):
                return idx
        