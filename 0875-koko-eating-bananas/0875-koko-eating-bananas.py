class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = -0
        right = piles[-1] + 1
        hour = 0
        
        while left + 1 < right:
            mid = (left + right)//2
            hour = 0
            for num in piles:
                hour += ceil(num/mid)
                
            if hour > h:
                left = mid
            else:
                right = mid
            # print(left,mid,right)
        return right