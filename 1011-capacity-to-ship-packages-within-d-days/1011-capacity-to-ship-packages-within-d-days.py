class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def daysToComplete(kg):
            total = 0
            day = 1
            for weight in weights:
                if weight > kg:
                    return False
                if total + weight > kg:
                    day += 1
                    total = 0
                total += weight
                
            return days >=day
        
        left = min(weights) -1 
        right = sum(weights) + 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            if daysToComplete(mid):
                right = mid
                
            else:
                left = mid
            
        return right
        