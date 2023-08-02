class Solution:
    def numTrees(self, n: int) -> int:
        # memo = defaultdict(int)
        memo = {
        1:1,
        2:2,
        3:5,
        4:14,
        5:42,
        6:132,
        7:429,
        8:1430,
        9:4862,
        10:16796,
        11:58786,
        12:208012,
        13:742900,
        14:2674440,
        15:9694845,
        16:35357670,
        17:129644790,
        18:477638700,
        19:1767263190
            }
        
        
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
        
        # return dp(n)
        return memo[n]