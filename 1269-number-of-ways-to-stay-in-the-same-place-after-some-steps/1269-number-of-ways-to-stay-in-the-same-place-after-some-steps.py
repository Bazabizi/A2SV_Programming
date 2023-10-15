class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        N = 10**9 + 7
        
        @cache
        def dp(val , step):
            if val < 0 or val > arrLen - 1:
                return  0
            if step == steps:
                if val == 0:
                    return 1
                return 0
            ans = dp(val , step + 1)
            if val > 0:
                ans += dp(val - 1 , step + 1)
            if val != arrLen - 1:
                ans += dp(val + 1 , step  + 1)
            
            return ans
                
            
        return (dp(0 , 0))%N