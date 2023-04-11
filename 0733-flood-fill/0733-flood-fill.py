class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        def inbound(row,col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])
        
        def  dfs(visited , row , col):
            
            visited.add((row,col))
            temp = image[row][col]
            image[row][col] = color
            
            for r ,c in direction:
                
                newRow = row + r
                newCol = col + c
                if inbound(newRow,newCol) and ( newRow , newCol ) not in visited and image[newRow][newCol] == temp:
                    dfs(visited , newRow, newCol)
        dfs(visited , sr ,sc)
        return image
            