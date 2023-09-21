class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = -1
        right = n + 1
        while left + 1 < right:
            mid = left + (right - left)//2
            val = mid*(1 + mid)//2
            if val > n:
                right = mid
            else:
                left = mid
                
        return left
            