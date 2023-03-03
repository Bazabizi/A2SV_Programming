class Solution:
    def mySqrt(self, x: int) -> int:
        left = -1 
        right = x + 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            if mid*mid < x:
                left = mid
            elif mid * mid > x :
                right = mid
            
            else:
                return mid
        return left