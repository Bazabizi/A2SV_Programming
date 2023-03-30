class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        val = 1
        count = 0
        while num >= val:
            if num & val:
                count += 1
            val <<= 1
            
        return count