class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = defaultdict(int)
        coins.sort()
        def dp(total):
            if total == 0:
                memo[total] = -1
                return 0
            if total < 0:
                return float('inf')
            if total in memo:
                return memo[total] + 1
            val =  float('inf')
            for num in coins:
                path = dp(total - num)
                val = min(val , path)
            memo[total] = val
            return memo[total] + 1
        
        ans = dp(amount)
        if ans == float('inf'):
            return -1
        return ans
            
        
     