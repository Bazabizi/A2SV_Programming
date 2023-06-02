class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minval = float('inf')
        maxval = float('inf')
        for val in nums:
            if minval > val:
                minval = val
            elif minval < val < maxval :
                maxval = val
            elif maxval < val:
                return True
        
        return False