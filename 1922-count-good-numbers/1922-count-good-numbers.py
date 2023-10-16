class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def multiply(a, b, m):
            return ((a % m) * (b % m)) % m

        def binary_exponentiation(base, exponent):
            result = 1
            while exponent > 0:
                if exponent & 1:
                    result = multiply(result , base , N)
                base = multiply(base , base , N)
                exponent >>= 1
            
            return result

        N = 10**9 + 7
        ans = 1
        half = n//2
        ans = binary_exponentiation(5 , half)
        ans %= N
        
        ans *= binary_exponentiation(4 , half)
        ans %= N
        if n%2: 
            ans *= 5
            
        return ans % N
            