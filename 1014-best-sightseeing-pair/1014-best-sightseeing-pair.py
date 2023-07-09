class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = [values[0] , 0]
        size = len(values)
        ans = 0
        for idx in range(1 , size):
            ans = max(ans , dp[0] + values[idx] + (dp[1] - idx))
            if dp[0] <= idx - dp[1] + values[idx]:
                dp = [values[idx] , idx]
        
        return ans
        