class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(idx , total):
            if idx >= len(coins):
                if total == amount:
                    return 1
                return 0
            if total > amount:
                return 0
            ans = 0
            ans += dp(idx + 1 , total)
            ans += dp(idx , total + coins[idx])
        
            return ans
    
        return dp(0 , 0)
        