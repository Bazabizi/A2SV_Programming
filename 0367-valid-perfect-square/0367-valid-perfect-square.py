class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = math.sqrt(num)
        if n != math.ceil(n) or n != math.floor(n):
            return False
        return True