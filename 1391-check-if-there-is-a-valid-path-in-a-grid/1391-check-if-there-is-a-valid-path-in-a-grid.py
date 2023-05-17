class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        parent = defaultdict(tuple)
        count = defaultdict(int)
        rowlength = len(grid)
        colLength = len(grid[0])
        
        connection = {1:[1 , -1 , 1 ,-1] ,
                      2:[-1 , 1 ,-1 , 1] ,
                      3:[1 , -1 , -1, 1] , 
                      4:[-1, -1 , 1 , 1] ,
                      5:[1 , 1 , -1 ,-1] , 
                      6:[-1 , 1 ,1 , -1] }
        
        for row in range(rowlength):
            for col in range(colLength):
                parent[(row ,col)] = (row , col)
                count[(row , col)] = 1
        
        def inbound(row , col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def find(child):
            while child != parent[child]:
                parent[child] = parent[parent[child]]
                child = parent[child]
            return child     
        
        def union(x , y):
            rep_x = find(x)
            rep_y = find(y)
            if rep_x != rep_y:
                if count[rep_x] >= count[rep_y]:
                    parent[rep_x] = rep_y
                    count[rep_y] += count[rep_x]
                else:
                    parent[rep_y] = rep_x
                    count[rep_x] += count[rep_y]
        
        for row in range(rowlength):
            for col in range(colLength):
                cur = grid[row][col]
                if inbound(row + 1 , col) and connection[cur][3] == 1 and connection[cur][3] == connection[grid[row+1][col]][1]:
                    union((row , col) , (row + 1 , col))
                if inbound(row , col + 1) and connection[cur][2] == 1 and connection[cur][2] == connection[grid[row][col + 1]][0]:
                    union((row , col) , (row , col + 1))
        return find((0 ,0)) == find((rowlength - 1 , colLength - 1))