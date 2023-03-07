class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def sufficient_Trip(times):
            trip = 0
            for t in time:
                trip += times//t
            
            return trip >= totalTrips
        
        left = 0
        right = max(time) * totalTrips
        
        while left + 1 < right :
            mid = left + (right - left) // 2
            
            if sufficient_Trip(mid):
                right = mid
            else:
                left = mid
        
        return right