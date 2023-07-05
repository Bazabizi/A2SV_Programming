class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        dp = [0]*size
        dp[0] = cost[0]
        dp[1] = cost[1]
        for idx in range(2 , size):
            dp[idx] += min(dp[idx- 1] , dp[idx - 2]) + cost[idx]
        
        return min(dp[-1] , dp[-2])