class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rowLength = len(dungeon)
        colLength = len(dungeon[0])
        for row in range(rowLength - 1 , -1 , -1):
            for col in range(colLength - 1 , -1 , -1):
                value = dungeon[row][col]
                val = float('inf')
                if row != rowLength - 1:
                    val = min(val , dungeon[row + 1][col])
                    
                if col != colLength - 1:
                    val = min(val  , dungeon[row][col + 1])
                
                if val == float('inf'):
                    val = 0
                dungeon[row][col] = val - value
                
                if dungeon[row][col] < 0 :
                    dungeon[row][col] = 0
        # print(dungeon)
        return dungeon[0][0] + 1