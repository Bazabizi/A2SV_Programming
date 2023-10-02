class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        counta , countb = 0 , 0
        maxA , maxB = 0 , 0
        
        for l in colors:
            if l == 'A':
                counta += 1
                if countb > 2:
                    maxB += countb - 2
                countb = 0
            if l == "B":
                if counta > 2:
                    maxA += counta - 2
                counta = 0
                countb += 1
        if countb > 2:
            maxB += countb - 2
        if counta > 2:
            maxA += counta - 2
                
        return maxA > maxB