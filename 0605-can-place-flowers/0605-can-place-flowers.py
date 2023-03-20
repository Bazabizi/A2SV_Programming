class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for idx , planted in enumerate(flowerbed):
            if planted == 0:
                if (idx == 0 or flowerbed[idx - 1] == 0) and (idx ==len(flowerbed) - 1 or flowerbed[idx + 1] == 0):
                    n -= 1
                    flowerbed[idx] = 1
                    
        return n <= 0