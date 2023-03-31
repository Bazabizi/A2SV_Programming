class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        one = False
        zero = False
        val = 1
        if n & val:
            one = True
        else:
            zero = True
        val <<= 1
        while val <= n:
            if zero:
                if n & val == 0:
                    return False
                one = True
                zero = False
            else:
                if n & val:
                    return False
                one = False
                zero = True
            val <<= 1
        
        return True