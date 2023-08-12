class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def canWarmAllHouses(radius):
            top = 0
            bottom = 0
            length_house = len(houses)
            length_heat = len(heaters)
            
            while top < length_house and bottom < length_heat:
                if abs(houses[top] - heaters[bottom]) <= radius:
                    top += 1
                else:
                    bottom += 1
            
            if bottom >= length_heat:
                return False
            
            return True
            

        houses.sort()
        heaters.sort()
        max_ = max(houses[-1] - heaters[0] , heaters[-1] - houses[0])
        left, right = 0, max_
        while left < right:
            mid = left + (right-left)//2
            if canWarmAllHouses(mid):
                right = mid
            else:
                left = mid+1
        return left

    
                
        
        