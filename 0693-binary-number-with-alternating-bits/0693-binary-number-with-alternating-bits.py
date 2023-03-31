class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bits = bin(n)
        return "00" not in bits and "11" not in bits