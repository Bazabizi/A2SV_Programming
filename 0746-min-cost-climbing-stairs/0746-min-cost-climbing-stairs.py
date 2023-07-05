class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        first = cost[0]
        second = cost[1]
        
        for idx in range(2 , size):
            val = min(first , second) + cost[idx]
            first = second
            second = val
            
        return min(second , first)