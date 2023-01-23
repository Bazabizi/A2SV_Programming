class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sum = 0
        length = len(piles)//3
        idx = len(piles)-2
        count = 0
        while count< length:
            sum +=piles[idx]
            idx -=2
            count+=1
        
        return sum
        