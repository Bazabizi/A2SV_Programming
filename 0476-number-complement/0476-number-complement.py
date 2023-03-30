class Solution:
    def findComplement(self, num: int) -> int:
        val = 1
        for _ in range(32):
            num = num ^ val
            val <<= 1
            if val > num:
                break
        return num