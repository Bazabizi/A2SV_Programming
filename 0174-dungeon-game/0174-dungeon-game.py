class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        
        dungeon[rows - 1][cols - 1] = max(1, 1 - dungeon[rows - 1][cols - 1])
        
        for row in range(rows - 2, -1, -1):
            dungeon[row][cols - 1] = max(1, dungeon[row + 1][cols - 1] - dungeon[row][cols - 1])
        
        for col in range(cols - 2, -1, -1):
            dungeon[rows - 1][col] = max(1, dungeon[rows - 1][col + 1] - dungeon[rows - 1][col])
        
        for row in range(rows - 2, -1, -1):
            for col in range(cols - 2, -1, -1):
                right = max(1, dungeon[row][col + 1] - dungeon[row][col])
                down = max(1, dungeon[row + 1][col] - dungeon[row][col])
                dungeon[row][col] = min(right, down)
        
        return dungeon[0][0]