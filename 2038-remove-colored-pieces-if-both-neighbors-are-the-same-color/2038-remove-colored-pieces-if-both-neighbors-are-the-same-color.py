class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) < 3:
            return False
        maxA, maxB = 0,0
        l, r = 0, 0
        while r < len(colors):
            c = colors[l]
            while r < len(colors) and c == colors[r]:
                r += 1
            if c == 'A':
                maxA += max(0, (r - l - 2))
            if c == 'B':
                maxB += max(0,(r - l -2) )
            l = r
        return maxA > maxB
            