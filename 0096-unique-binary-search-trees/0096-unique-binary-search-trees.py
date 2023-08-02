class Solution:
    def numTrees(self, n: int) -> int:
        memo = defaultdict(int)
        
        def dp(n):
            if n == 0 or n == 1:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = 0
            for num in range(1 , n + 1):
                minval = num - 1
                maxval = n - num
                memo[n] += dp(minval) * dp(maxval)
            
            return memo[n]
        
        return dp(n)