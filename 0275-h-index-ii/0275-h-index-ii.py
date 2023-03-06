class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def Hindex(h):
            count = 0
            for num in citations[::-1]:
                if h <= num:
                    count += 1
                    
            return count < h
                
        left = -1
        right = citations[-1] + 1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if Hindex(mid):
                right = mid
            else:
                left = mid
        
        return left