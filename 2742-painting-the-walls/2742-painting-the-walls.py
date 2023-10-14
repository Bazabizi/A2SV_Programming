class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
        @cache
        def dp(idx , remain):
            if remain <= 0:
                return 0
            if idx == len(cost):
                return float('inf')
            
            return min(cost[idx] + dp(idx + 1 , remain - 1 - time[idx]) , dp(idx + 1 , remain))
        return dp(0 , len(cost))