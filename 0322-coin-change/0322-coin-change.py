class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] *( amount + 1)
        if amount == 0:
            return 0
        for num in coins:
            if num <= amount:
                dp[num] = 1
            
        for num in range(1 , amount + 1):
            for coin in coins:
                if num - coin >= 0:
                    dp[num] = min (dp[num] , dp[num - coin] + 1)
        
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]