class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        @cache
        def dp( idx , a , b):
            num = len(costs)
            if idx >= num:
                if a > num//2 or b > num//2:
                    return float('inf')
                return 0
            
            left = dp(idx + 1 , a + 1 , b) + costs[idx][0]
            right = dp(idx + 1 , a  , b + 1) + costs[idx][1]
        
            return min(left , right)
        
        return dp(0 , 0 ,0)
            
            
            