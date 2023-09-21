class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num + 1
        
        while left + 1 < right:
            mid = left + (right - left)//2
            val = mid*mid
            if val < num:
                left = mid
            elif val > num:
                right= mid
            else:
                return True
        
        return False