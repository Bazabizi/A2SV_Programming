class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sum = 0
        size = len(piles)
        length = len(piles)//3
        for idx in range(length,size,2):
            sum += piles[idx]
        
        return sum
        