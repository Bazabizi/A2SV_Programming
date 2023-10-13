class Solution:
    def countOrders(self, n: int) -> int:
        N= 10**9 + 7
        return (factorial(2*n) // (2**n))% N