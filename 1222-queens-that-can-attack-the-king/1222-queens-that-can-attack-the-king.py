class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        '''
        
          x  y 
          
          x - 1     y      (-1, 0)
          x + 1     y      (1, 0)
          x   y - 1
          x  y + 1
          x - 1  y - 1
          x + 1  y
          
          directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1),(-1, 1), (-1, -1)]
          (1, 0)
          king 
        '''
        queenSet=set(map(tuple,queens))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1),(-1, 1), (-1, -1)]
        ans=[]
        
        for dx ,dy in directions:
            curX=king[0]
            curY=king[1]
            
            while curX>=0 and curY>=0 and curX<8 and curY<8:
                if (curX, curY) in queenSet:
                    ans.append([curX,curY])
                    break
                curX += dx
                curY += dy
        
        return ans
        
        
        